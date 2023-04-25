import unittest
from my_labs.lab10.lab10_1 import Quick_find


class Test_Quick_find(unittest.TestCase):
    def test_union(self):
        snm = Quick_find()
        for i in range(5):
            snm.make_set()
        for i in range(5):
            snm.union(1, i)
        self.assertEqual(str(snm), '1 1 1 1 1')

    def test_connected(self):
        snm = Quick_find()
        for i in range(5):
            snm.make_set()
        for i in range(3):
            snm.union(1, i)
        self.assertTrue(snm.connected(1, 2))
        self.assertFalse(snm.connected(1, 4))

    def test_err(self):
        snm = Quick_find()
        snm.make_set()
        snm.make_set()
        with self.assertRaises(IndexError) as e:
            snm.union(1,3)


