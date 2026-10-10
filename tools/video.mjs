#!/usr/bin/env node
// Render an animated HTML design to MP4, frame by frame (deterministic, no
// screen recording). Animate with CSS animations / Web Animations; the tool
// pauses them all and seeks each frame. A page can also define
// window.seek(seconds) for JS-driven motion.
//
//   node tools/video.mjs reel.html [--size 1080x1920] [--fps 30] [--duration 12]
//                                  [--audio music.mp3] [--out reel.mp4] [--alpha]
//
// --alpha renders a transparent overlay (ProRes 4444 .mov) to lay over footage
// with ffmpeg's overlay filter; the page must leave its background transparent.
// Duration defaults to <meta name="duration" content="12">, else the end of the
// longest animation. Needs ffmpeg on PATH.
import { spawn } from 'node:child_process';
import { basename, dirname, extname, join } from 'node:path';
import { parseArgs, parseSize, launch, toUrl, applyFrame, settle } from './lib.mjs';

const args = parseArgs(process.argv.slice(2));
const file = args._[0];
if (!file) {
  console.error('usage: node tools/video.mjs reel.html [--size 1080x1920] [--fps 30] [--duration s] [--audio f] [--out f.mp4]');
  process.exit(1);
}

const size = parseSize(args.size || '1080x1920');
const fps = Number(args.fps || 30);
const alpha = Boolean(args.alpha);
const out = args.out || join(dirname(file), `${basename(file, extname(file))}-${size.w}x${size.h}.${alpha ? 'mov' : 'mp4'}`);

const browser = await launch();
try {
  const page = await browser.newPage({ viewport: { width: size.w, height: size.h } });
  await page.goto(toUrl(file));
  await applyFrame(page, size);
  await settle(page);

  const seek = (ms) => page.evaluate((ms) => {
    for (const a of document.getAnimations()) { a.pause(); a.currentTime = ms; }
    if (typeof window.seek === 'function') window.seek(ms / 1000);
  }, ms);
  await seek(0);

  const duration = Number(args.duration) || await page.evaluate(() => {
    const meta = Number(document.querySelector('meta[name=duration]')?.content);
    if (meta) return meta;
    const ends = document.getAnimations().map((a) => a.effect.getComputedTiming().endTime)
      .filter((t) => Number.isFinite(t));
    return ends.length ? Math.max(...ends) / 1000 : 5;
  });
  const frames = Math.round(duration * fps);

  const ff = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-'];
  if (args.audio) ff.push('-i', args.audio, '-shortest', '-c:a', 'aac', '-b:a', '192k');
  if (alpha) ff.push('-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', out);
  else ff.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', '-movflags', '+faststart', out);
  const enc = spawn('ffmpeg', ff, { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => enc.on('close', (c) => (c ? rej(new Error(`ffmpeg exited ${c}`)) : res())));

  for (let f = 0; f < frames; f++) {
    await seek((f / fps) * 1000);
    const buf = await page.screenshot(alpha ? { type: 'png', omitBackground: true } : { type: 'jpeg', quality: 92 });
    if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once('drain', r));
    if (f % fps === 0) process.stderr.write(`\r${(f / fps).toFixed(0)}s / ${duration}s`);
  }
  enc.stdin.end();
  await done;
  process.stderr.write('\n');
  console.log(out);
} finally {
  await browser.close();
}
