import unittest
from unittest import main
from my_labs.lab6.lab6_5 import partition
from my_labs.lab6.lab6_5 import quickSort
from my_labs.lab6.lab6_5 import quickSort


class Test_quick_sort(unittest.TestCase):
    def test_normal1(self):
        A = [1, 0, 24, 12, 33, 25, 11, 11, 11, 0]
        quickSort(A)
        self.assertEqual(A, [0, 0, 1, 11, 11, 11, 12, 24, 25, 33])


    def test_sorted(self):
        A = [0, 1, 11, 12, 342, 500, 1000 ]
        quickSort(A)
        self.assertEqual(A,[0, 1, 11, 12, 342, 500, 1000])


    def test_inverse(self):
        A = [6, 5, 4, 3, 2, 1]
        quickSort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])


    def test_normal(self):
        A = [1, 1, 1, 2, 2, 1, 3, 0, 0,]
        quickSort(A)
        self.assertEqual(A, [0, 0, 1, 1, 1, 1, 2, 2, 3])


    def test_normal(self):
        A = [0, 100, 11, 1, 1, 23, 45, 63, 564, 1000]
        quickSort(A)
        self.assertEqual(A, [0, 1, 1, 11, 23, 45, 63, 100, 564, 1000])


    def test_empty(self):
        A = []
        quickSort(A)
        self.assertEqual(A, [])


    def test_same_elements(self):
        A = [1, 1, 1, 1, 1, 1]
        quickSort(A)
        self.assertEqual(A, [1, 1, 1, 1, 1, 1])


    def test_almost_same_elements(self):
        A = [1, 1, 0, 0, 2, 2, 0, 0, 3, 3, 1, 1, 1, 1]
        quickSort(A)
        self.assertEqual(A, [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3])


    def test_one_element(self):
        A = [1]
        quickSort(A)
        self.assertEqual(A, [1])


    def test_except1(self):
        with self.assertRaises(TypeError) as e:
            quickSort('dsadsadsadsad')


    def test_except2(self):
        with self.assertRaises(TypeError) as e:
            quickSort((1, 2, 0, 1, 5))


if __name__ == '__main__':
    main()
