import unittest
from my_labs.lab9.lab9_4 import shutting_yard


class Test_shutting_yard(unittest.TestCase):
    def testf_ops(self):
        self.assertEqual(shutting_yard('( 2 + 3 * ( 1 + 2 ) ) ** 2'), '2 3 1 2 + * + 2 **')


    def test_ops2(self):
        self.assertEqual(shutting_yard('( 1 + 2 / 4 + 25 ) ** 2'), '1 2 4 / + 25 + 2 **')


    def test_empty(self):
        self.assertEqual(shutting_yard(''), '')


    def test_one_element(self):
        self.assertEqual(shutting_yard('1'), '1')


    def test_ops3(self):
        self.assertEqual(shutting_yard('( 2 + 3 )'), '2 3 +')

