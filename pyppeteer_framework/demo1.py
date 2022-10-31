import asyncio
from pyppeteer import launch


async def main():
    # 浏览器 启动参数
    params = {
        "executablePath": "D:\chrome-win\chrome.exe",
        # 关闭无头浏览器 默认是无头启动的
        "headless": False
    }
    # 创建浏览器对象，可以传入 字典形式参数
    browser = await launch(**params)

    # 创建一个页面对象， 页面操作在该对象上执行
    page = await browser.newPage()

    # 页面跳转
    await page.goto('https://new.qq.com/rain/a/20211031A01O0H00')

    # 页面内容
    page_text = await page.content()
    print(page_text)

    # 关闭浏览器对象
    await browser.close()
# 创建异步池并执行main函数。
asyncio.get_event_loop().run_until_complete(main())