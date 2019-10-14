from django.test import TestCase
import unittest


def sub(a,b):
    return a-b


#必须继承unittest.TestCase
class TestSub(unittest.TestCase):
    """
    用例必须以test_开头，且每个用例名不能相同;用例执行的时候会自动执行test开头的用例
    用例中不能传参和调用，但可以在用例中调用自定义的方法
    """
    def setUp(self):
        print("测试开始执行前")
    def tearDown(self):
        print("测试结束执行后")

    def test_sub1(self):
        result = sub(3,2)
        print("test_sub1")
        self.assertEqual(result,1)

    def test_sub2(self):
        result = sub(3.2,2.2)
        print("test_sub2")
        self.assertEqual(result,1.0)






if __name__ =="__main__":
    unittest.main()#执行全部的用例
