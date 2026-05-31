import { chromium } from 'playwright';
const ctx = await chromium.launchPersistentContext('/tmp/pwprofile2', {
  headless: true,
  viewport: { width: 1280, height: 720 },
  recordVideo: { dir: '/workspace/glottos-auto/vid', size: { width: 1280, height: 720 } },
  args: ['--no-sandbox','--disable-dev-shm-usage']
});
const page = ctx.pages()[0] || await ctx.newPage();
await page.goto('https://example.com', { waitUntil: 'load' });
await page.waitForTimeout(2500);
await ctx.close();
console.log('navigated + recorded OK');
