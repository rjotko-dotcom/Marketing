#!/usr/bin/env node
// Screenshot a real page (an app, a landing page) at phone size, for use
// inside designs. Real screens beat invented ones.
//
//   node tools/shot.mjs https://example.com [--size 384x832] [--scale 3]
//                       [--wait 1500] [--full] [--dark] [--out shot.png]
//                       [--storage state.json] [--click "css selector"]
//                       [--hide "css selector, ..."]
//
// --storage seeds the page before it loads, so an app shows real-looking data
// instead of its empty first-run screen. JSON shape:
//   { "localStorage": { "key": value }, "sessionStorage": { "key": value } }
// Non-string values are JSON-encoded. --click taps an element (e.g. a tab)
// before the shot; repeat it by separating selectors with " >> then >> ".
// --hide removes stray UI (toasts, cookie bars) from the shot. Service workers
// are blocked so "update ready" prompts never appear.
import { readFileSync } from 'node:fs';
import { parseArgs, parseSize, launch, toUrl } from './lib.mjs';

const args = parseArgs(process.argv.slice(2));
const target = args._[0];
if (!target) {
  console.error('usage: node tools/shot.mjs URL [--size 384x832] [--scale 3] [--wait ms] [--full] [--dark] [--out f.png]');
  process.exit(1);
}

const size = parseSize(args.size || '384x832');
const browser = await launch();
try {
  const page = await browser.newPage({
    viewport: { width: size.w, height: size.h },
    deviceScaleFactor: Number(args.scale || 3),
    isMobile: size.w < 800,
    hasTouch: size.w < 800,
    colorScheme: args.dark ? 'dark' : 'light',
    serviceWorkers: 'block',
  });
  if (args.storage) {
    const state = JSON.parse(readFileSync(args.storage, 'utf8'));
    await page.addInitScript((state) => {
      for (const [area, entries] of Object.entries(state)) {
        for (const [k, v] of Object.entries(entries || {})) {
          window[area].setItem(k, typeof v === 'string' ? v : JSON.stringify(v));
        }
      }
    }, state);
  }
  await page.goto(toUrl(target), { waitUntil: 'networkidle' });
  await page.waitForTimeout(Number(args.wait || 1500));
  if (args.click) {
    for (const sel of String(args.click).split(' >> then >> ')) {
      await page.locator(sel).first().click();
      await page.waitForTimeout(800);
    }
  }
  if (args.hide) await page.addStyleTag({ content: `${args.hide} { display: none !important; }` });
  const out = args.out || 'shot.png';
  await page.screenshot({ path: out, fullPage: Boolean(args.full) });
  console.log(out);
} finally {
  await browser.close();
}
