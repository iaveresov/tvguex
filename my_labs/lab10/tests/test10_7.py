import unittest
from my_labs.lab10.lab10_7 import parent, shift_up


class Test_shift_up(unittest.TestCase):
    def test_positive1(self):
        heap = [5, 10, 11, 12, 14, 20, 21, 14, 16, 15, 10]
        shift_up(heap, 10)
        self.assertEqual(heap, [5, 10, 11, 12, 10, 20, 21, 14, 16, 15, 14])


    def test_positive2(self):
        heap = [5, 10, 11, 12, 14, 20, 21, 14, 16, 15, 3]
        shift_up(heap, 10)
        self.assertEqual(heap, [3, 5, 11, 12, 10, 20, 21, 14, 16, 15, 14])

    def test_positive3(self):
        heap = [5, 10, 11, 12, 14, 20, 21, 14, 16, 15, 15]
        shift_up(heap, 10)
        self.assertEqual(heap, [5, 10, 11, 12, 14, 20, 21, 14, 16, 15, 15])

    def test_positive4(self):
        heap = [5, 10, 11, 12, 9, 20, 21, 14, 16, 15, 15]
        shift_up(heap, 4)
        self.assertEqual(heap, [5, 9, 11, 12, 10, 20, 21, 14, 16, 15, 15])