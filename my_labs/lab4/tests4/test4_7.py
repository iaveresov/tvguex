import unittest
from unittest import main
from my_labs.lab4.lab4_7 import count_sort


class Test_count_sort(unittest.TestCase):
    def test_normal(self):
        A = [1, 543, 1000, 994, 465, 10, 15]
        count_sort(A)
        self.assertEqual(A, sorted([1, 543, 1000, 994, 465, 10, 15]))


    def test_sorted(self):
        A = [1, 234, 432, 500, 657, 1000]
        count_sort(A)
        self.assertEqual(A, [1, 234, 432, 500, 657, 1000])

    def test_inverse(self):
        A = [1000, 777, 554, 425, 12, 1, 0]
        count_sort(A)
        self.assertEqual(A, [0, 1, 12, 425, 554, 777, 1000])


    def test_same_elements1(self):
        A = [1000, 1000, 1000, 1000]
        count_sort(A)
        self.assertEqual(A, [1000, 1000, 1000, 1000])


    def test_same_elements2(self):
        A = [1, 1, 1, 1, 1]
        count_sort(A)
        self.assertEqual(A, [1, 1, 1, 1, 1])

    def test_empty(self):
        A = []
        count_sort(A)
        self.assertEqual(A, [])


    def test_one_element(self):
        A = [1]
        count_sort(A)
        self.assertEqual(A, [1])


    def test_except1(self):
        with self.assertRaises(TypeError) as e:
            count_sort((1, 0, 423, 1000))

    def test_except2(self):
        with self.assertRaises(TypeError) as e:
            count_sort([1, 2, None, 234, 32])


    def test_almost_same_elements(self):
        A = [100, 100, 1000, 1000, 1000, 100, 1000, 1000]
        count_sort(A)
        self.assertEqual(A, [100, 100, 100, 1000, 1000, 1000, 1000, 1000])


if __name__ == '__name__':
    main()