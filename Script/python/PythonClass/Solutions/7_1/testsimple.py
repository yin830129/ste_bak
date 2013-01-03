# testsimple.py

import simple
import unittest

class TestAdd(unittest.TestCase):
    def testint(self):
        r = simple.add(2,3)
        self.assertEquals(r,5)
    def teststr(self):
        r = simple.add("Hello","World")
        self.assertEquals(r,"HelloWorld")
    def testfloat(self):
        r = simple.add(2.1,3.4)
        self.assertEquals(r,5.5)
    def testTypeError(self):
        self.assertRaises(TypeError,simple.add,3,"Hello")
    def testTypeErrorMessage(self):
        try:
            simple.add(3,"Hello")
        except TypeError as e:
            self.assertEquals(str(e),"unsupported operand type(s) for +: 'int' and 'str'")

class TestSub(unittest.TestCase):
    def testint(self):
        r = simple.sub(3,2)
        self.assertEquals(r,1)
    def testfloat(self):
        r = simple.sub(2.6,1.1)
        self.assertEquals(r,1.5)

if __name__ == '__main__':
    unittest.main()
