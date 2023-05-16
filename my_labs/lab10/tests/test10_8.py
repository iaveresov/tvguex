import unittest
from my_labs.lab10.lab10_8 import left_son, right_son, min_son, sift_down


class Test(unittest.TestCase):
    def test_positive1(self):
        heap = [15, 10, 11, 13, 11, 14, 26, 16, 17, 14]
        sift_down(heap, 0)
        self.assertEqual(heap, [10, 11, 11, 13, 14, 14, 26, 16, 17, 15])

    def test_postitive2(self):
        heap = [1, 2, 4, 6, 5, 10, 24, 6, 7, 8, 10, 11, 23, 21, 25]
        sift_down(heap, 6)
        self.assertEqual(heap, [1, 2, 4, 6, 5, 10, 21, 6, 7, 8, 10, 11, 23, 24, 25])


    def test_positive3(self):
        heap = [1, 2, 4, 6, 5, 10, 24, 6, 7, 8, 10, 11, 23, 21]
        sift_down(heap, 6)
        self.assertEqual(heap, [1, 2, 4, 6, 5, 10, 21, 6, 7, 8, 10, 11, 23, 24])

    def test_positive4(self):
        heap = [1, 2, 4, 6, 5, 10, 21, 6, 7, 8, 10, 11, 23, 24]
        sift_down(heap, 6)
        self.assertEqual(heap, [1, 2, 4, 6, 5, 10, 21, 6, 7, 8, 10, 11, 23, 24])