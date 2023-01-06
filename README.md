# python_test_automation_framework

## 介绍

· 自动化测试框架，即是应用于自动化测试所用的框架。自动化测试框架要么是提供可重用的基础自动化测试模块，如：selenium、watir等，它们主要提供最基础的自动化测试功能，比如打开一个程序，模拟鼠标和键盘来点击或操作被测试对象，最后验证被测对象的属性以判断程序的正确性；要么是可以提供自动化测试执行和管理功能的架构模块，如：Phoenix Framework，robot，STAF等，它们本身不提供基础的自动化测试支持，只是用于组织、管理和执行那些独立的自动化测试用例，测试完成后统计测试结果，通常这类框架一般都会集成一个基础自动化测试模块，如：robot框架就可以集成selenium框架，Phoenix Framework集成的也是selenium框架；  
· 基于Python3.11的自动化单元测试框架。只需要进行一些适用性和效率参数的调整，这些自动化测试框架就能够开箱即用，大大节省了开发时间。而且由于这些框架被广泛使用，他们具有很好的健壮性，并且具有广泛多样的用例集和技术来轻易发现微小的缺陷。

## 什么是框架

框架是整个或部分系统的可重用设计，表现为一组抽象构件及构件实例间交互的方法；另一种定义认为，框架是可被应用开发者定制的应用骨架。前者是从应用方面，而后者是从目的方面给出的定义。从框架的定义可以了解，框架可以是被重用的基础平台；框架也可以是组织架构类的东西。其实后者更为贴切，因为框和架本来就是组织和归类所用的。

## 测试框架优点

1. 代码复用 ，将基础的测试代码封装，从而降低代码的复杂性。
2. 提高维护效率，有效组织和管理测试脚本。
3. 快速实现项目的自动化测试，不用从0开始，一般测试框架完成后，其他类似程序也可以快速复用。
4. 输出各种美观易懂的测试报告。

## 安装教程

Python 3.11

## Python3.11 自动化测试框架

Pytest、Robot Framework和UnitTest主要用于功能与单元测试，Lettuce和Behave仅适用于行为驱动测试。如果已经有了一定的Pytest经验，那么请使用Pytest-bdd。

1. [behave](behave_framework/README.md)

*

2. [Doctest](doctest_framework/README.md)

*

3. [lettuce](lettuce_framework/README.md)

*

4. [mock unittest](mock_unittest_framework/README.md)

*

5. [Nose](nose_framework/README.md)

*

6. [py.test](pytest_framework/README.md)

*

7. [pytest-bdd](pytest_bdd_framework/README.md)

*

8. [robot](robot_framework/README.md)

*

8. [selenium](selenium_framework/README.md)

9. [tox](tox_framework/README.md)

*

10. [Unittest2](unittest2_framework/README.md)

*

11. [Unittest](unittest_framework/README.md)

## 其他工具

### [2to3](https://docs.python.org/3/library/2to3.html)

