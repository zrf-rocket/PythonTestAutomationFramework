# python_Pyppeteer_framework

## 介绍
是Puppeteer的Python版本的实现，但他不是 Google 开发的，是一位来自于日本的工程师依据 Puppeteer 的一些功能开发出来的非官方版本。  
Puppeteer是Google基于Node.js开发的一个工具，有了它我们可以通过 JavaScript 来控制 Chrome 浏览器的一些操作，当然也可以用作网络爬虫上，其 API 极其完善，功能非常强大。[参见Puppeteer的代码示例]()

## 软件架构
软件架构说明


## 安装和使用
>pip install pyppeteer -i https://pypi.douban.com/simple  
>chromium下载地址：https://npm.taobao.org/mirrors/chromium-browser-snapshots/

#### 浏览器启动参数
```
executablePath	    str	    chrome.exe运行的路径
ignorehttpserrrors	bool	忽略https错误，默认false
headless	        bool	True 开始无头浏览器 False关闭无头
dumpio	            bool	设置True 解决浏览器多开卡死 （没有测试过）


args的参数设置
–disable-infobars	        -	                关闭自动化提示框
–window-size=1920,1080	    str	                设置浏览器大小吗，1920是宽，1080是宽
–log-level=30	            str	                日志保存等级， 建议设置越好越好，要不然生成的日志占用的空间会很大 30为warning级别
–start-maximized	        -	                窗口最大化模式
–proxy-server=http://localhost:1080	    str	    设置代理
userDataDir=D:\userData\	            str	    用户文件保存地址


ignoreHTTPSErrors (bool):   是否要忽略 HTTPS 的错误，默认是 False。
headless (bool):            是否启用 Headless 模式，即无界面模式，如果 devtools 这个参数是 True 的话，那么该参数就会被设置为 False，否则为 True，即默认是开启无界面模式的。
executablePath (str):       可执行文件的路径，如果指定之后就不需要使用默认的 Chromium 了，可以指定为已有的 Chrome 或 Chromium。
slowMo (int|float):         通过传入指定的时间，可以减缓 Pyppeteer 的一些模拟操作。
args (List[str]):           在执行过程中可以传入的额外参数。
ignoreDefaultArgs (bool):   不使用 Pyppeteer 的默认参数，如果使用了这个参数，那么最好通过 args 参数来设定一些参数，否则可能会出现一些意想不到的问题。这个参数相对比较危险，慎用。
handleSIGINT (bool):        是否响应 SIGINT 信号，也就是可以使用 Ctrl + C 来终止浏览器程序，默认是 True。
handleSIGTERM (bool):       是否响应 SIGTERM 信号，一般是 kill 命令，默认是 True。
handleSIGHUP (bool):        是否响应 SIGHUP 信号，即挂起信号，比如终端退出操作，默认是 True。
dumpio (bool):              是否将 Pyppeteer 的输出内容传给 process.stdout 和 process.stderr 对象，默认是 False。
userDataDir (str):          即用户数据文件夹，即可以保留一些个性化配置和操作记录。
env (dict):                 环境变量，可以通过字典形式传入。
devtools (bool):            是否为每一个页面自动开启调试工具，默认是 False。如果这个参数设置为 True，那么 headless 参数就会无效，会被强制设置为 False。
logLevel (int|str):         日志级别，默认和 root logger 对象的级别相同。
autoClose (bool):           当一些命令执行完之后，是否自动关闭浏览器，默认是 True。
loop (asyncio.AbstractEventLoop): 时间循环对象。
```