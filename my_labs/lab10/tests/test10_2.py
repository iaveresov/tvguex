import unittest
from my_labs.lab10.lab10_2 import UnionFind

class Test_UnionFind(unittest.TestCase):
    def test_union1(self):
        uf = UnionFind()
        for i in range(6):
            uf.make_set()
        for i in range(3):
            uf.union_set(1, i)
        for i in range(3):
            uf.union_set(2, i + 3)
        self.assertEqual(str(uf), '1 1 1 1 1 1')

    def test_union2(self):
        uf = UnionFind()
        for i in range(6):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(1, 2)
        self.assertEqual(str(uf), '0 1 1 2 4 5')

    def test_root(self):
        uf = UnionFind()
        for i in range(6):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(1, 2)
        self.assertEqual(uf.root(3), 1)


    def test_connected(self):
        uf = UnionFind()
        for i in range(6):
            uf.make_set()
        uf.union_set(2, 3)
        uf.union_set(1, 2)
        self.assertTrue(uf.connected(1, 3))
        self.assertTrue(uf.connected(3, 1))
        self.assertFalse(uf.connected(5, 0))
        self.assertFalse(uf.connected(0, 5))
