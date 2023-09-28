#Python selenium framework

## 介绍
1. Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera，Edge等。这个工具的主要功能包括：测试与浏览器的兼容性——测试应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成.Net、Java、Perl等不同语言的测试脚本。
2. selenium 本身是一套web自动化测试工具，但其经常被用于爬虫，解决一些复杂爬虫的问题。Selenium 用于爬虫时，相当于模拟人操作浏览器。

参见：[官方网站](https://www.selenium.dev/)


## 功能特点
1. Selenium测试直接在浏览器中运行，就像真实用户所做的一样。Selenium测试可以在Windows、Linux和Macintosh上的Internet Explorer、Chrome和Firefox中运行。其他测试工具都不能覆盖如此多的平台。
2. Selenium完全开源，对商业用户也没有任何限制，支持分布式，拥有成熟的社区与学习文档。
3. 通过编写模仿用户操作的Selenium测试脚本，可以从终端用户的角度来测试应用程序。通过在不同浏览器中运行测试，更容易发现浏览器的不兼容性。
4. Selenium的核心，也称browser bot，是用JavaScript编写的。这使得测试脚本可以在受支持的浏览器中运行。browser bot负责执行从测试脚本接收到的命令，测试脚本要么是用HTML的表布局编写的，要么是使用一种受支持的编程语言编写的。
5. 框架底层使用JavaScript模拟真实用户对浏览器进行操作。测试脚本执行时，浏览器自动按照脚本代码做出点击，输入，打开，验证等操作，就像真实用户所做的一样，从终端用户的角度测试应用程序。 
6. 使浏览器兼容性测试自动化成为可能，尽管在不同的浏览器上依然有细微的差别。
7. 使用简单，可使用Java，Python等多种语言编写用例脚本。

## 安装
pip install selenium==4.5.0

## 使用
```
使用 selenium 需要先安装 浏览器驱动，selenium 支持多种浏览器
注意: linux中浏览器驱动要安装对应的linux版本
驱动要放到环境变量的地址里，如 C:\Program Files\Python311，或者把驱动的地址放到环境变量里。
```

#### 浏览器驱动
> [chrome 谷歌](http://chromedriver.storage.googleapis.com/index.html)  
> [ie，IE不好用](http://selenium-release.storage.googleapis.com/index.html)  
> [firefox，火狐](https://github.com/mozilla/geckodriver/releases/)  
> phantomjs，这是一个无界面的浏览器，特点是高效
> safari，手机浏览器




