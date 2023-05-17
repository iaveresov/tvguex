import unittest
from my_labs.lab7.lab7_9 import MyQueue

class Test_queue(unittest.TestCase):
    def test_enqueue(self):
        A = MyQueue()
        for i in range(5):
            A.enqueue(1)
        self.assertEqual(str(A), '[1, 1, 1, 1, 1, None, None, None, None, None]')
        for i in range(5):
            A.enqueue(1)
        self.assertEqual(A.enqueue(1), False)

    def test_dequeue(self):
        A = MyQueue()
        self.assertEqual(A.dequeue(), None)
        for i in range(10):
            A.enqueue(i)
        self.assertEqual(A.dequeue(), 0)
        for i in range(1, 9):
            self.assertEqual(A.dequeue(), i)

    def test_is_empty(self):
        A = MyQueue()
        self.assertTrue(A.isEmpty())
        for i in range(10):
            A.enqueue(i)
        self.assertFalse(A.isEmpty())
        for i in range(10):
            A.dequeue()
        self.assertTrue(A.isEmpty())

    def test_enqueue_cyclic(self):
        A = MyQueue()
        for i in range(10):
            A.enqueue(i)
        for i in range(6):
            A.dequeue()
        for i in range(10, 16):
            A.enqueue(i)
        self.assertEqual(str(A), '[10, 11, 12, 13, 14, 15, 6, 7, 8, 9]')

    def test_dequeue_cyclic(self):
        A = MyQueue()
        for i in range(10):
            A.enqueue(i)
        for i in range(6):
            A.dequeue()
        for i in range(10, 16):
            A.enqueue(i)
        for i in range(4):
            A.dequeue()
        self.assertEqual(str(A), '[10, 11, 12, 13, 14, 15, None, None, None, None]')
        for i in range(3):
            A.dequeue()
        self.assertEqual(str(A), '[None, None, None, 13, 14, 15, None, None, None, None]')