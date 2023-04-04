import unittest
from unittest import main
from my_labs.lab7.lab7_1 import binSearchRec
from my_labs.lab7.lab7_1 import binSearch


class Test_bin_search(unittest.TestCase):
    def test_normal(self):
        A = [0, 2, 3, 8, 9, 10, 11, 14, 23, 28]
        self.assertEqual(binSearch(A, 11), '9 14 10 11')