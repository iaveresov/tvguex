import unittest
from my_labs.lab10.lab10_3 import UnionFind


class Test_UnionFind(unittest.TestCase):
    def test_union(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(3, 4)
        uf.union_set(5, 6)
        uf.union_set(6, 7)
        uf.union_set(7, 8)
        uf.union_set(4, 5)
        self.assertEqual(str(uf), '0 1 5 2 2 5 5 5 5 9' + '\n' + '1 1 3 1 1 7 1 1 1 1')

    def test_root(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(3, 4)
        uf.union_set(5, 6)
        uf.union_set(6, 7)
        uf.union_set(7, 8)
        uf.union_set(4, 5)
        self.assertEqual(uf.root(2), 5)

    def test_connected(self):
        uf = UnionFind()
        for i in range(10):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(3, 4)
        uf.union_set(5, 6)
        uf.union_set(6, 7)
        uf.union_set(7, 8)
        uf.union_set(4, 5)
        self.assertTrue(uf.connected(3, 8))
        self.assertFalse(uf.connected(2, 9))