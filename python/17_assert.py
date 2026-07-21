assert len("Hi")==2
assert 1+2>6  # 报错

import unittest
# 测试代码和实现代码一般写在不同文件中
# 所以需要在测试文件中，把需要测试的函数、类等引入进来
from my_calculator import my_add  # from 文件名 import 函数名/类名
class TestMyAdd(unittest.TestCase): # 继承各种测试功能
    def test_add(self):
        self.assertEqual(my_add(1,2),3)
    # 测试函数必须以 test_ 开头！

"""
在终端：python -m unittest
运行所有继承自unittest的所有子类中的test_开头的测试代码
. 表示通过测试
F 表示没有通过测试
"""

"""
assertEqual(A,B)    assert A==B
assertTrue(A)       assert A is True
assertFalse(A)      assert A is False
assertNotIn(2,[1,3,-1])  assert 2 in [1,3,-1]
"""

