#Python unittest framework

## 介绍
1. UnitTest/PyUnit一种标准化的针对单元测试的Python类自动化测试框架。基类TestCase提供了各种断言方法、以及所有清理和设置的例程。因此，TestCase子类中的每一种方法都是以“test”作为名词前缀，以标识它们能够被作为测试用例所运行。用户可以使用load方法和TestSuite类来分组、并加载各种测试。
2. 可以通过联合使用，来构建自定义的测试运行器。正如我们使用Junit去测试Selenium那样，UnitTest也会用到UnitTest-sml-reporting、并能生成各种XML类型的报告。
3. 是python内置的标准类库，它的API跟java的Junit、.net的NUnit、C++的CppUnit很相似，通过继承unittest.TestCase来创建一个测试用例。

参见：[官方文档](https://docs.python.org/3.11/library/unittest.html)

## 特点
    1. 使用断言判断返回布尔值来判断期望值和实际值的差异。
    2. 可以构建共同的初始化变量或实例。
    3. 框架结构可以组织用例批量运行。

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

