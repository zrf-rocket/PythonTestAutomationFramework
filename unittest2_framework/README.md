#Python unittest2 framework

## 介绍
是Unittest的升级版本，对API进行了改善以及更好的诊断语法。

>参见：[unittest2的详细文档](https://pypi.python.org/pypi/unittest2)

## 特点


## 功能概念
1. test fixture  
   一个test fixture表示执行一个或多个测试前的准备工作，以及执行完成后清理工作。例如：创建临时或代理数据库或目录，或者是一个启动服务器进程。
2. test case  
   一个test case是一个独立的测试单元，它检查特定输入是否响应特定的输出，unittest提供了一个基本类——TestCase，这个类用于创建一个或多个test case。
3. test suite  
   一个test suite是test cases、或test suites、或者两者的一个集合，它用于把想执行tests放在一起。
4. test runner  
   一个test runner是由两部分成分：合理安排tests的执行、提供给user输出结果。runner可以用一个图形界面、文本、或者是一个特殊的值，代表tests执行的结果。

## 目录
* common 公共函数  
  公共函数、方法以及通用操作的管理。
* config 配置文件目录  
  存放所有使用的配置文件，实现配置与代码分离。
* data 测试数据目录  
  将所有的用例参数化使用的文件放到这里，一般可采用xlsx、csv、xml等格式。实现数据与代码分离。
* drivers 驱动目录  
  一般存放浏览器驱动，如如Chromedriver等。
* logs 日志目录  
  存放运行时日志和错误日志error log等。
* report 测试报告  
  管理和存放程序运行后生成的测试报告，一般可有html报告、excel报告等。
* testcase 测试用例  
  测试用例管理功能，可以分模块编写，建相应的目录。


