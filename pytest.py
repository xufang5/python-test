import unittest

def add(x, y):

    return x+y

class Test(unittest.TestCase):
    def test_add1(self):
        a = 1
        b = 1
        self.assertEquals(add(a, b),2)
    def test_add2(self):
        a = 1.0
        b = 1.0
        self.assertEquals(add(a, b),2.0)


if __name__ =="__main__":

    unittest.main()
