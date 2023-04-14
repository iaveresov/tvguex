import unittest
from my_labs.lab9.lab9_1 import make_operation
from my_labs.lab9.lab9_1 import calculate_ops


class Test_ops(unittest.TestCase):
    def test_calculate1(self):
        self.assertEqual(calculate_ops('12 12 + 4 /'), 6)

    def test_calculate2(self):
        self.assertEqual(calculate_ops('12 11 - 2 ** 24 +'), 25)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(Exception) as e:
            calculate_ops('12 21 + 1 1 - /')

    def test_calculate_power(self):
        self.assertEqual(calculate_ops('12 2 **'), 144)
