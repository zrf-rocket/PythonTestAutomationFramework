import unittest
from unittest import (
    TestCase,
    TestSuite,
    TestResult,
    TestLoader,
    TestProgram,
    FunctionTestCase,
    BaseTestSuite
)


class TestStringMethods(TestCase):
    def test_upper(self, s: str = "unittest"):
        self.assertEqual(s.upper(), "UNITTEST")
        # self.assertEquals()

    def test_isupper(self):
        self.assertTrue("UNITTEST".isupper())
        self.assertFalse("Unittest".isupper())
        # 数据类型判断
        self.assertTupleEqual((12, "unittext"), (12, "unittext"))
        self.assertDictEqual({"name": "python"}, {"framework": "unittest"})
        self.assertListEqual([1, 23, 23.45], ["213", "framework"])
        self.assertSetEqual(set1=set('python'), set2=set(1))

    def test_split(self, s: str = "this is unittest framework"):
        self.assertEqual(s.split(), ['this', 'is', 'unittest', 'framework'])
        with self.assertRaises(TypeError):
            print(s.split(2))


if __name__ == '__main__':
    unittest.main()
