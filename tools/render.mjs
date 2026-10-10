#!/usr/bin/env node
// Render an HTML design to PNG at one or more sizes.
//
//   node tools/render.mjs design.html [--size 1080x1350,1080x1920] [--out dir] [--scale 1]
//
// Sizes default to <meta name="sizes" content="1080x1080,1080x1350">, else 1080x1080.
// A design with several [data-slide] elements (a carousel) renders one PNG per
// slide; only the current slide is shown. Output: <name>-<w>x<h>[-<n>].png.
import { mkdirSync } from 'node:fs';
import { basename, dirname, extname, join } from 'node:path';
import { parseArgs, parseSize, launch, toUrl, applyFrame, settle } from './lib.mjs';

const args = parseArgs(process.argv.slice(2));
const file = args._[0];
if (!file) {
  console.error('usage: node tools/render.mjs design.html [--size 1080x1350,...] [--out dir] [--scale 1]');
  process.exit(1);
}

const browser = await launch();
try {
  const scale = Number(args.scale || 1);
  const probe = await browser.newPage();
  await probe.goto(toUrl(file));
  const metaSizes = await probe.evaluate(() => document.querySelector('meta[name=sizes]')?.content);
  await probe.close();

  const sizes = String(args.size || metaSizes || '1080x1080').split(',').map(parseSize);
  const outDir = args.out || dirname(file);
  mkdirSync(outDir, { recursive: true });
  const name = basename(file, extname(file));

  for (const size of sizes) {
    const page = await browser.newPage({ viewport: { width: size.w, height: size.h }, deviceScaleFactor: scale });
    await page.goto(toUrl(file));
    await applyFrame(page, size);
    await settle(page);
    const slides = await page.locator('[data-slide]').count();
    const runs = slides || 1;
    for (let i = 0; i < runs; i++) {
      if (slides) {
        await page.evaluate((i) => document.querySelectorAll('[data-slide]').forEach((el, n) => {
          el.style.display = n === i ? '' : 'none';
        }), i);
      }
      const suffix = slides ? `-${String(i + 1).padStart(2, '0')}` : '';
      const out = join(outDir, `${name}-${size.w}x${size.h}${suffix}.png`);
      await page.screenshot({ path: out, animations: 'disabled' });
      console.log(out);
    }
    await page.close();
  }
} finally {
  await browser.close();
}
