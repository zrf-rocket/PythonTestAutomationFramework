import asyncio
from pyppeteer import launch


async def main():
    # 浏览器启动参数
    params = {
        "executablePath": "D:\chrome-win\chrome.exe",
        "headless": False,

        "args": [
            '--disable-infobars',  # 关闭自动化提示框
            # '--window-size=1920,1080',  # 窗口大小
            '--log-level=30',  # 日志保存等级， 建议设置越好越好，要不然生成的日志占用的空间会很大 30为warning级别
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',  # UA
            '--no-sandbox',  # 关闭沙盒模式
            '--start-maximized',  # 窗口最大化模式
            # '--proxy-server=http://localhost:1080'  # 代理
            r'userDataDir=D:\userdata'  # 用户文件地址
        ],
    }
    browser = await launch(**params)
    page = await browser.newPage()
    await page.goto('https://www.httpbin.org/headers')
    page_text = await page.content()
    print(page_text)
    input('----------------')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
