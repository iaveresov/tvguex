import unittest
from my_labs.lab7.lab7_9 import MyQueue

class Test_queue(unittest.TestCase):
    def test_enqueue(self):
        A = MyQueue()
        for i in range(10):
            A.enqueue(i)
        self.assertFalse(A.enqueue(1))

7