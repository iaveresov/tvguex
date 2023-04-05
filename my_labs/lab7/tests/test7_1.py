import unittest
from unittest import main
from my_labs.lab7.lab7_1 import binSearchRec
from my_labs.lab7.lab7_1 import binSearch


class Test_bin_search(unittest.TestCase):
    def test_normal1(self):
        A = [0, 2, 3, 8, 9, 10, 11, 14, 23, 28]
        self.assertEqual(binSearch(A, 11), '9 14 10 11')


    def test_normal2(self):
        A = [2, 4, 7, 9, 15, 16, 20, 21, 22, 28, 29]
        self.assertEqual(binSearch(A, 13), '16 7 9 15')


    def test_same_elements(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(binSearch(A, 1), '1')


    def test_negative_more(self):
        A = [1, 5, 10, 21, 45, 64]
        self.assertEqual(binSearch(A, 65), None)


    def test_negative_less(self):
        A = [13, 14, 16, 56, 64]
        self.assertEqual(binSearch(A, 12), None)


    def test_string(self):
        A = 'abcdefgh'
        self.assertEqual(binSearch(A, 'e'), 'd f e' )

    def test_empty(self):
        self.assertEqual(binSearch([], 1), None)

