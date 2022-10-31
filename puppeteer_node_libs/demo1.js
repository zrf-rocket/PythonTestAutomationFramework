//跳转到https://example.com 并保存截图至 demo1.png
const puppeteer = require('puppeteer');
(async() => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://example.com');
    await page.screenshot({path:'demo1.png'});
    await browser.close();
})();