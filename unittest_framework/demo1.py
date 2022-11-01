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
    def test_upper(self,s:str="unittest"):
        self.assertEqual(s.upper(), "UNITTEST")
        # self.assertEquals()

    def test_isupper(self):
        self.assertTrue("UNITTEST".isupper())
        self.assertFalse("Unittest".isupper())
        # 数据类型判断
        # self.assertTupleEqual()
        # self.assertDictEqual()
        # self.assertListEqual()
        # self.assertSetEqual()

    def test_split(self, s: str = "this is unittest framework"):
        self.assertEqual(s.split(), ['this', 'is', 'unittest', 'framework'])
        with self.assertRaises(TypeError):
            print(s.split(2))

if __name__ == '__main__':
    unittest.main()
