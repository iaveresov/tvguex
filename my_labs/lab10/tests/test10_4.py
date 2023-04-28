import unittest
from my_labs.lab10.lab10_4 import UnionFind


class  Test_UnionFind(unittest.TestCase):
    def test_union_set(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(1, 2)
        uf.union_set(5, 6)
        self.assertEqual(str(uf), '0 1 1 3 4 5 5 7 8 9\n0 1 0 0 0 1 0 0 0 0')
        uf.union_set(2, 6)
        self.assertEqual(str(uf), '0 1 1 3 4 1 5 7 8 9\n0 2 0 0 0 1 0 0 0 0')

    def test_root(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(1, 2)
        uf.union_set(5, 6)
        uf.union_set(8, 9)
        uf.union_set(2, 9)
        self.assertEqual(uf.root(9), 1)
    def test_connected(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(1, 2)
        uf.union_set(5, 6)
        self.assertTrue(uf.connected(1, 2))
        self.assertFalse(uf.connected(2, 3))
        uf.union_set(2, 6)
        self.assertTrue(uf.connected(6, 1))