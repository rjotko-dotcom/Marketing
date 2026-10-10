// Shared helpers for the render tools. Chromium comes from Playwright; set
// CHROMIUM_PATH to use a browser that is already installed (cloud sessions:
// /opt/pw-browsers/chromium).
import { chromium } from 'playwright';
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

export function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next === undefined || next.startsWith('--')) args[key] = true;
      else { args[key] = next; i++; }
    } else args._.push(a);
  }
  return args;
}

export function parseSize(s) {
  const m = /^(\d+)x(\d+)$/.exec(String(s).trim());
  if (!m) throw new Error(`bad size "${s}" — use WIDTHxHEIGHT, e.g. 1080x1350`);
  return { w: +m[1], h: +m[2] };
}

export async function launch() {
  const executablePath = process.env.CHROMIUM_PATH;
  return chromium.launch(executablePath ? { executablePath } : {});
}

export function toUrl(target) {
  if (/^https?:\/\//.test(target)) return target;
  const p = resolve(target);
  if (!existsSync(p)) throw new Error(`no such file: ${target}`);
  return pathToFileURL(p).href;
}

// Lets a design adapt to the frame it is rendered at: --w/--h in px, --u is
// 1% of the shorter side, and data-shape is square | portrait | story | landscape.
export async function applyFrame(page, { w, h }) {
  await page.evaluate(({ w, h }) => {
    const r = h / w;
    const shape = r > 1.6 ? 'story' : r > 1.05 ? 'portrait' : r < 0.95 ? 'landscape' : 'square';
    const el = document.documentElement;
    el.style.setProperty('--w', `${w}px`);
    el.style.setProperty('--h', `${h}px`);
    el.style.setProperty('--u', `${Math.min(w, h) / 100}px`);
    el.dataset.shape = shape;
  }, { w, h });
}

export async function settle(page) {
  await page.evaluate(() => document.fonts && document.fonts.ready);
  await page.evaluate(() => Promise.all([...document.images].map((img) =>
    img.complete ? null : new Promise((r) => { img.onload = img.onerror = r; }))));
}
