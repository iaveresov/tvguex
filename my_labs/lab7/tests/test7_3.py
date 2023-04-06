import unittest
from my_labs.lab7.lab7_3 import fibSearch
from my_labs.lab7.lab7_3 import fibSearchRec


class Test_fib_search(unittest.TestCase):
    def test_normal1(self):
        A = [3, 4, 7, 10, 13, 16, 18, 19]
        self.assertEqual(fibSearch(A, 8), '7 13 10 10')

    def test_normal2(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(fibSearch(A, 5), '3 5')

    def test_normal3(self):
        A = [1, 7, 10, 15, 18, 24]
        self.assertEqual(fibSearch(A, 15), '10 18 15')
    def test_empty(self):
        A = []
        self.assertEqual(fibSearch(A, 0), None)

    def test_same_elements(self):
        A = [1, 1, 1, 1, 1, 1]
        self.assertEqual(fibSearch(A, 1), '1')

    def test_one_element(self):
        A = [1]
        self.assertEqual(fibSearch(A, 1), '1')