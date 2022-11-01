#Python pytest-bdd framework

## 介绍
pytest-bdd实现了一些Gherkin语言，用于自动化测试的需要，更简单的BDD(behaviora driven development)开发。  
pytest-bdd中所有pytest的功能都可以使用。



## 特点
```
① 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考。
② 能够支持简单的单元测试和复杂的功能测试。
③ 支持参数化。
④ 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败。
⑤ 支持重复执行失败的case。
⑥ 支持运行由nose, unittest编写的测试case。
⑦ 具有很多第三方插件，并且可以自定义扩展。
⑧ 方便的和持续集成工具集成。
```

## 安装
pip install pytest-bdd

## 目录
pytest-bdd的项目结构实际上是非常灵活的（因为它是基于pytest）
1. 所有的测试代码都应该写在tests的文件夹中
2. 所有的feature文件定义在 features文件夹中 
3. Step Definition模块应该定义在测试的子目录中命名为step_defs
4. conftest.py文件应该位于和step definition相同的目录

大型测试套件可以把具有相同功能的feature和step def定义在子目录中。pytest能够发现测试目录下的所有测试。

## 使用
pytest -s -v test_web.py
