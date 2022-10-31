const puppeteer = require('puppeteer');
// const puppeteer_core = require('puppeteer-core');
// const {TimeoutError} = require('puppeteer/Errors');

try{
    await page.waitForSelector('.foo');
}catch (e) {
    if (e instanceof TimeoutError){

    }
}