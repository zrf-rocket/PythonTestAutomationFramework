//将指定页面创建成一个PDF
const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://new.qq.com/rain/a/20211031A01O0H00', {waitUntil: 'networkidle2'});
    await page.pdf({path:'demo2.pdf', format: 'A4'});
    await browser.close();
})();