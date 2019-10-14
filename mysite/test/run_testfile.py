import unittest
import os

test_dir = os.path.dirname(os.path.abspath(__file__))
#运行以test_开头的测试文件
suit = unittest.defaultTestLoader.discover(test_dir, "test_*.py")
runner = unittest.TextTestRunner()
runner.run(suit)
