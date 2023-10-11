# ABOUT

**【关于我们】**

* [Articulate v1.0](https://mp.weixin.qq.com/s/0yqGBPbOI6QxHqK17WxU8Q)
* [Articulate v2.0](https://mp.weixin.qq.com/s/V5Axn-ZWi22ubh5Jiocb9g)

[![](https://img.shields.io/badge/GitHub-zrf--rocket-blue?logo=gitpod)](https://github.com/zrf-rocket)
[![](https://img.shields.io/badge/Gitee-SteveRocket-pink)](https://gitee.com/SteveRocket/)
![CTO Plus](https://img.shields.io/badge/微信公众号：CTO%20Plus-8A2BE2) 🥰

## Contact

![微信公众号](./static/wechat.png)  
**< 微信公众号 >**

![QQ技术交流群](./static/qq_link.png)  
**< QQ技术交流群 >**

![联系作者](./static/wechat.jpg)  
**< 联系作者 >**

## **【代码工程系列】**

* [Python和Go的设计模式](https://github.com/zrf-rocket/DesignPattern)
    * GitHub：https://github.com/zrf-rocket/DesignPattern
    * Gitee：https://gitee.com/SteveRocket/design_pattern

* [Python、Go的编码技巧cookbook](https://github.com/zrf-rocket/CookBook)
    * GitHub：https://github.com/zrf-rocket/CookBook
    * Gitee：https://gitee.com/SteveRocket/cook-book

* [Go代码示例](https://github.com/zrf-rocket/PracticeGo)
    * GitHub：https://github.com/zrf-rocket/PracticeGo
    * Gitee：https://gitee.com/SteveRocket/practice_go

* [Python代码示例](https://github.com/zrf-rocket/PracticePython)
    * GitHub：https://github.com/zrf-rocket/PracticePython
    * Gitee：https://gitee.com/SteveRocket/practice_python

* [Python Web框架的示例代码](https://github.com/zrf-rocket/PythonFramework)
    * GitHub：https://github.com/zrf-rocket/PythonFramework
    * Gitee：https://gitee.com/SteveRocket/python_framework

* [Rust代码示例](https://github.com/zrf-rocket/PracticeRust)
    * GitHub：https://github.com/zrf-rocket/PracticeRust
    * Gitee：https://gitee.com/SteveRocket/practice_rust

* [Vue代码示例](https://github.com/zrf-rocket/PracticeVue)
    * GitHub：https://github.com/zrf-rocket/PracticeVue
    * Gitee：https://gitee.com/SteveRocket/practice_vue

* [前端代码示例](https://github.com/zrf-rocket/PracticeFronted)
    * GitHub：https://github.com/zrf-rocket/PracticeFronted
    * Gitee：https://gitee.com/SteveRocket/practice_fronted

* [Python自动化测试框架](https://github.com/zrf-rocket/PythonTestAutomationFramework)
    * GitHub：https://github.com/zrf-rocket/PythonTestAutomationFramework
    * Gitee：https://gitee.com/SteveRocket/python_test_automation_framework

* [Python和Go的算法代码示例](https://github.com/zrf-rocket/Algorithms)
    * GitHub：https://github.com/zrf-rocket/Algorithms
    * Gitee：https://gitee.com/SteveRocket/Algorithms

* [Python和Go的数据结构代码示例](https://github.com/zrf-rocket/DataStructure)
    * GitHub：https://github.com/zrf-rocket/DataStructure
    * Gitee：https://gitee.com/SteveRocket/data_structure

* [编码规范](https://github.com/zrf-rocket/DevGuide)
    * GitHub：https://github.com/zrf-rocket/DevGuide
    * Gitee：https://gitee.com/SteveRocket/develop_guide

* [编码安全规范](https://github.com/zrf-rocket/SecGuide)
    * GitHub：https://github.com/zrf-rocket/SecGuide
    * Gitee：https://gitee.com/SteveRocket/security_guide

**【产品系列】**

* [主机监控系统-日志收集与报警管理系统（SIEM）](https://github.com/zrf-rocket/SIEM)
    * GitHub：https://github.com/zrf-rocket/SIEM
    * Gitee：https://gitee.com/SteveRocket/siem

* [安全运营中心（SOC）-终端侦测与响应系统（EDR）](https://github.com/zrf-rocket/EDR_SOC)
    * GitHub：https://github.com/zrf-rocket/EDR_SOC
    * Gitee：https://gitee.com/SteveRocket/edr_soc

* [DevSecOps-SDLC](https://github.com/zrf-rocket/DevSecOps-SDLC)
    * GitHub：https://github.com/zrf-rocket/DevSecOps-SDLC
    * Gitee：https://gitee.com/SteveRocket/dev-sec-ops-sdlc

* [AI图像识别-智能缺陷检测系统]()
    * [基于AI图像识别的工业缺陷检测应用系统（GPU&FPGA）](https://mp.weixin.qq.com/s/04qefQFg-Pg1Gcqq1vBLQQ)
    * [基于AI图像识别的智能缺陷检测系统，在钢铁行业的应用-技术方案](https://mp.weixin.qq.com/s/dSHbnuOwQZzE4CvPr1JYjg)



# python_test_automation_framework

## 介绍

* 自动化测试框架是用于自动化执行测试的工具、库和约定的集合。它们可用于构建、指导或促进测试过程，使测试人员可以快速有效地进行测试。
* 自动化测试框架，即应用于自动化测试所用的框架。自动化测试框架要么是提供可重用的基础自动化测试模块，如：selenium、watir等，它们主要提供最基础的自动化测试功能，比如打开一个程序，模拟鼠标和键盘来点击或操作被测试对象，最后验证被测对象的属性以判断程序的正确性；要么是可以提供自动化测试执行和管理功能的架构模块，如：Phoenix Framework，robot，STAF等，它们本身不提供基础的自动化测试支持，只是用于组织、管理和执行那些独立的自动化测试用例，测试完成后统计测试结果，通常这类框架一般都会集成一个基础自动化测试模块，如：robot框架就可以集成selenium框架，Phoenix Framework集成的也是selenium框架；  
* 使用基于Python3.11的自动化单元测试框架。只需要进行一些适用性和效率参数的调整，这些自动化测试框架就能够开箱即用，大大节省了开发时间。而且由于这些框架被广泛使用，他们具有很好的健壮性，并且具有广泛多样的用例集和技术来轻易发现微小的缺陷。

## 什么是框架

框架是整个或部分系统的可重用设计，表现为一组抽象构件及构件实例间交互的方法；另一种定义认为，框架是可被应用开发者定制的应用骨架。前者是从应用方面，而后者是从目的方面给出的定义。从框架的定义可以了解，框架可以是被重用的基础平台；框架也可以是组织架构类的东西。其实后者更为贴切，因为框和架本来就是组织和归类所用的。

## 测试框架优点

1. 代码复用 ，将基础的测试代码封装，从而降低代码的复杂性。
2. 提高维护效率，有效组织和管理测试脚本。
3. 快速实现项目的自动化测试，不用从0开始，一般测试框架完成后，其他类似程序也可以快速复用。
4. 输出各种美观易懂的测试报告。
5. 自动化程度高：测试框架可以高度自动化，提高测试效率，避免手动测试出现的错误和遗漏。
6. 可重复性强：测试框架能够对相同的测试用例进行反复测试，保证测试结果的稳定和一致性。
7. 软件测试覆盖率高：测试框架能够对软件进行全面测试，尽可能地覆盖所有场景，提高软件的质量。
8. 场景模拟能力强：测试框架可以模拟各种场景，例如负载、并发、网络等，有效地检测软件的性能和稳定性。
9. 与持续集成配合使用：测试框架可以与持续集成系统结合使用，实现自动化测试和自动化发布，提高开发和发布效率。
10. 提高团队协作效率：测试框架可以提供测试团队协作和交流的平台，以方便测试项目的管理和进度监控。

## 安装教程

Python 3.11
pip install -r requirements.txt

## 单元测试上给对象打补丁
给对象打补丁指的是在单元测试中使用 mock 或 stub 对象来替代实际对象的某些行为或属性，以便于测试其它部分的代码。

比如，在一个单元测试中，如果某个对象的某个属性是一个时间戳，这个属性值在每次运行时都会改变，导致测试结果难以预测。这时可以使用 patch 库中的 patch 函数来打补丁，替换掉这个属性的返回值，使测试更稳定可靠。

示例代码：

```python
import unittest
from unittest.mock import patch

class TestMyClass(unittest.TestCase):
    @patch('my_module.MyClass.my_method')
    def test_something(self, mock_method):
        mock_method.return_value = "mocked_value"
        
        obj = my_module.MyClass()
        result = obj.my_method()
        
        self.assertEqual(result, "mocked_value")
```

通过使用 patch 函数和 MagicMock 对象来模拟 MyClass 类中的 my_method 方法，使其返回一个预定值。在测试代码中，我们首先导入 patch 函数和 MagicMock 类，然后在 test_something 方法中使用 patch 函数来打补丁，指定要模拟的目标为 my_module.MyClass.my_method，然后在方法里实例化 MyClass 对象，并调用 my_method 方法。此时，由于已经打了补丁，my_method 方法将返回我们指定的预定值，而不是本来的行为。最后，使用 assertEqual 断言来确认测试结果是否符合预期。

## 单元测试中测试异常情况
单元测试中测试异常情况非常重要，因为它确保代码可以处理各种不同的输入情况，并且能够具有良好的错误处理和回复机制。以下是一些测试异常情况的技巧：

1.考虑所有可能的异常情况：在测试中，确保涉及代码的每个路径都覆盖到相关异常情况。这些可能包括无效的参数、未处理异常、系统资源耗尽等等。

2.测试代码逻辑：测试是否有异常情况会导致代码逻辑不正确。在这种情况下，需要编写测试来检查代码是否接受预期的异常条件和对该条件的响应是否是正确的。

3.断言异常：使用断言来确保代码在遇到异常时能够产生预期结果。例如，可以断言特定类型的异常被抛出，或者代码是否正确地处理了异常。

4.测试异常消息：测试异常消息是否明确和有用，以便开发人员易于诊断和修复错误。

有些代码可能会抛出异常，在测试过程中，我们需要模拟这种异常情况来确保代码的健壮性。例如，在 Python 中，可以使用 assertRaises 方法来测试代码是否抛出了预期的异常。
```python
def test_my_function_with_exception():
    with pytest.raises(ValueError):
        my_function_with_exception()
```
使用 pytest 的 assertRaises 方法来测试 my_function_with_exception() 是否会抛出 ValueError 异常。如果抛出了该异常，测试就通过了；否则就会失败。

总之，测试异常情况可以帮助开发人员减少代码中的漏洞和错误，并大大提高系统的质量和可靠性。

## 基准测试

* 基准测试是一种评估软件或硬件性能的测试方法，通过运行特定任务或程序来测量系统的性能和效率。基准测试通常包含多个测试项目，例如CPU速度、内存读写速度、图形处理器性能等，这些测试项目可以用来衡量计算机、移动设备或其他硬件设备的总体性能。比如想知道程序在哪里花费的时间，并进行计时测量。
* 在基准测试中，同一任务或程序在不同的硬件或软件环境下运行，测试结果可以被用作比较不同系统或硬件的性能和效能的依据。基准测试可以帮助用户和生产厂商选择最适合自己需要的硬件或软件系统。

## Python3.11 自动化测试框架

Pytest、Robot Framework和UnitTest主要用于功能与单元测试，Lettuce和Behave仅适用于行为驱动测试。如果已经有了一定的Pytest经验，那么请使用Pytest-bdd。
1. [behave](https://behave.readthedocs.io/en/latest/)  
behave是一个行为驱动开发(BDD)测试框架，适用于测试人员和开发人员在团队协作中使用。它支持Gherkin语言，可以让测试代码更直观易于理解。
* 优点：易于使用、提供了 BDD 支持、自然语言风格的语法、可与 Python 集成、可与其他工具（如 Selenium）集成、可扩展性强 
* 缺点：性能可能低、文档不太全面 


2. [Doctest](https://docs.python.org/3/library/doctest.html)   
Doctest是Python标准库中的模块，可以将代码示例作为文档测试的一部分执行，并将其与实际结果进行比较。适用于小规模的单元测试和文档编写。
* 优点：内置于 Python 标准库、易于使用、可用于文档和测试、可以把测试与代码整体编写 
* 缺点：不能进行复杂的测试、测试结果的可读性不够好 


3. [lettuce](https://lettuce.io/)   
lettuce是一种基于BDD的Python测试框架，它支持Gherkin语言并集成了Selenium和BeautifulSoup等工具。适用于Web开发和应用程序的测试。
基于Gherkin语言编写的场景描述文件，可以自动生成测试代码，提供HTML测试报告。

* 优点：易于起步，无需编写代码；灵活性高，支持多种自然语言；可与其它 Python 测试库集成；可扩展性强 
* 缺点：文档不太全面，社区的活跃度较低 


4. [mock unittest](https://docs.python.org/3/library/unittest.mock.html)  
mock unittest是一个用于Python的测试框架，可以为其它测试编写的测试添加mock对象。适用于需要模拟（mock）对象的情况下。
* 优点：易于使用、支持多种测试形式、可以单独使用或与 unittest、nosetest 和 pytest 结合使用 
* 缺点：某些文档不太好（但社区还是比较活跃），难以验证代码中复杂的依赖关系 


5. [Nose](https://nose.readthedocs.io/en/latest/)  
Nose是一个更加高级的Python测试框架，支持测试套件的自动化发现、扩展插件、多进程执行等功能。适用于大型、复杂的项目。
基于unittest的测试框架，可以自动搜寻测试模块、跑测试用例、产生测试报告等。

* 优点：易于使用、具有扩展性、可与 Python 测试库集成、提供插件系统、支持插件扩展 
* 缺点：有时文档不太好理解, 性能和可扩展性可能不如 Pytest 


6. [robot framework](http://robotframework.org/)  
一种基于关键字驱动的自动化测试框架，可以使用Python或Java语言编写关键字库，支持测试数据和测试结果的管理、关键字重用，支持多种测试用例风格。
robot framework是一个通用的自动化测试工具，支持关键字驱动测试（KDT）、数据驱动测试（DDT）、BDD等测试方法。适用于Web、桌面和移动应用程序的测试。
* 优点：易于起步，可快速构建测试用例；使用关键字的方式，让测试代码变得更加简洁易懂；提供了广泛的支持库；支持多种测试类型；可扩展性强；可与 Selenium 结合执行测试 
* 缺点：部分测试代码需要使用 Robot Framework 的 DSL，需要额外学习成本 


7. [py.test](https://pytest.org/en/stable/)  
一个功能强大的测试框架，可以自动产生测试报告，支持参数化、fixture、mock等，以及与其他工具如 Jenkins、Travis CI 等集成。
py.test是一个轻量级的Python测试框架，支持参数化、fixture、插件等特性。适用于小规模，需要快速运行测试的项目。
* 优点：易于使用、具有扩展性、可与 Python 测试库集成、提供插件系统、支持插件扩展，文档较全面 
* 缺点：某些访问可能不太友好 


8. [pytest-bdd](https://pytest-bdd.readthedocs.io/en/latest/)  
pytest-bdd是一个插件，使得开发者可以将pytest和behave相结合来进行BDD测试。适用于通过结合BDD和pytest来更好地组织和执行测试用例的情况下。
* 优点：易于起步，使用自然语言编写测试用例很容易；可扩展性强；可与 Selenium 结合执行测试 
* 缺点：需要额外学习成本，部分代码需要使用特定的 DSL 


9. [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)  
PyAutoGUI是一个支持跨平台的Python自动化GUI库，可以用于图像识别，模拟用户在屏幕上的鼠标和键盘操作。适用于GUI测试和UI自动化测试、自动截图等。 
* 优点：跨平台、易于安装和使用、提供详细的文档和教程、支持键盘、鼠标和屏幕的自动化操作 
* 缺点：性能可能不够高、易受屏幕分辨率和设置的影响 


10. [robot](https://github.com/robotframework/robotframework)  
robot是一个基于Python的自动化测试框架，提供了Web自动化测试、Android自动化测试、iOS自动化测试等功能。适用于Web、移动应用和桌面应用的自动化测试。
* 优点：使用关键字方式（DSL）让测试代码更易于编写与维护；具有丰富的库，支持多种测试类型；可与 Selenium 组合使用执行测试 
* 缺点：DSL 语言需要适应，需要额外的学习成本 


11. [selenium](https://www.selenium.dev/)  
selenium是一个开源的Web自动化测试框架，提供了丰富的API和支持多种编程语言的客户端库。适用于Web应用程序的测试。
* 优点：支持多种编程语言和多种 Web 浏览器；高度模块化，使得测试非常灵活； 提供详细的文档和教程 
* 缺点：速度有时可能偏慢， Web 应用程序的改变可能导致测试案例需要更改 


12. [tox](https://tox.readthedocs.io/en/latest/)  
tox是一个用于Python项目的测试工具，可以自动在多个虚拟环境中进行测试和部署。适用于Python项目发布和测试。
* 优点：轻松处理多个 Python 版本和依赖项；能够自动为每个 Python 版本和依赖项运行测试；基于配置文件简单而灵活 
* 缺点：文档可能不太全面，虚拟环境的设置可能比较麻烦 


13. [Unittest2](https://github.com/unittest-cpp/unittest-cpp)  
Unittest2是Python标准库中unittest模块的扩展，提供了许多新的特性和功能。适用于Python的单元测试。
* 优点：在 Python 标准库中可用；具有完整的测试框架功能；支持多种测试类型；可以与 Pycharm 等第三方工具集成 
* 缺点：文档可能不太全面，且与 Python 2 版本绑定 


14. [Unittest](https://docs.python.org/3/library/unittest.html)  
Unittest是Python标准库（内置）中的模块，可以进行单元测试、模块测试、支持测试套件、断言、测试装置等功能。适用于小型Python项目的测试。

* 优点：在 Python 标准库中可用；支持多种测试类型；具有完整的测试框架功能；可以与 Pycharm 等第三方工具集成 
* 缺点：文档可能不太友好， 有时出现令人困惑的错误信息。

使用Unittest在Django项目中的单元测试实战参考：
* [《Django单元测试：PGSQL数据库配置、常用测试工具、DB冲突方案和代码覆盖率实战》](https://blog.csdn.net/zhouruifu2015/article/details/129640284)
* [《Django单元测试：unittest、测试用例、断言方法总结》](https://blog.csdn.net/zhouruifu2015/article/details/129640243)


## 其他框架

Python其他开发框架参考：[Python常用开发框架Framework(WEB、测试、爬虫)总结](https://blog.csdn.net/zhouruifu2015/article/details/129855458)

## 其他工具

### [2to3](https://docs.python.org/3/library/2to3.html)

在最新的Python版本Python3.12中已经被废弃。
