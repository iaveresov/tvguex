import unittest
from my_labs.lab7.lab7_2 import interpolSearch
from my_labs.lab7.lab7_2 import interpolSearchRec

class Test_interpol_search(unittest.TestCase):
    def test_normal(self):
        A =[1, 4, 7, 8, 10, 17, 21, 23, 26, 32, 36, 40, 41, 43, 44, 47, 49]
        self.assertEqual(interpolSearch(A, 8), '7 8')


    def test_negative(self):
        A = [2, 4, 7, 9, 15, 16, 20, 21, 22, 28, 29]
        self.assertEqual(interpolSearch(A, 13), '15')


    def test_same_elements(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(interpolSearch(A, 1), '1')


    def test_negative_more(self):
        A = [1, 5, 10, 21, 45, 64]
        self.assertEqual(interpolSearch(A, 65), None)


    def test_negative_less(self):
        A = [13, 14, 16, 56, 64]
        self.assertEqual(interpolSearch(A, 12), None)

    def test_string_except(self):
        with self.assertRaises(TypeError) as e:
            interpolSearch('abcdefgh', 'e')
