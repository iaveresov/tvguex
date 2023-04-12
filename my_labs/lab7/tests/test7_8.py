import unittest
from my_labs.lab7.lab7_8 import MyStack

class Test_stack(unittest.TestCase):
    def test_push(self):
        A = MyStack()
        for i in range(10):
            self.assertTrue(A.push(i))
        self.assertFalse(A.push(11))

    def test_pop(self):
        A = MyStack()
        self.assertEqual(A.pop(), None)
        for i in range(10):
            A.push(i)
        self.assertEqual(A.pop(), 9)

    def test_is_empty(self):
        A = MyStack()
        self.assertTrue(A.isEmpty())
        for i in range(10):
            A.push(i)
        self.assertFalse(A.isEmpty())