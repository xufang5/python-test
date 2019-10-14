from django.test import TestCase
import unittest

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#必须继承unittest.TestCase
class TestAdd(unittest.TestCase):
    """
    用例必须以test_开头，且每个用例名不能相同;用例执行的时候会自动执行test开头的用例
    用例中不能传参和调用，但可以在用例中调用自定义的方法
    """
    def setUp(self):
        print("测试开始执行前")
    def tearDown(self):
        print("测试结束执行后")

    def test_add1(self):
        sum = add(1,2)
        print("test_add1")
        self.assertEqual(sum,3)

    def test_add2(self):
        sum = add(1.1,2.2)
        print("test_add2")
        self.assertEqual(sum,3.3)

    def test_add3(self):
        sum = add(-1,2)
        print("test_add3")
        self.assertEqual(sum,1)

    def test_add4(self):
        sum = add("Hello","world")
        print("test_add4")
        self.assertEqual(sum,"Helloworld")


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

    def test_sub1(self):
        result = sub(3.2,2.2)
        print("test_sub2")
        self.assertEqual(result,1.1)






if __name__ =="__main__":
    #unittest.main()#执行全部的用例

    #测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestSub("test_sub1"))#运行TestSub类中的test_sub1用例
    #测试运行
    runner = unittest.TextTestRunner()
    runner.run(suit)
