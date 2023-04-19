import unittest
from my_labs.lab9.lab9_5 import makeEdges
from my_labs.lab9.lab9_5 import make_graph
from my_labs.lab9.lab9_5 import prefix
from my_labs.lab9.lab9_5 import postfix


class Test_pr_ps(unittest.TestCase):
    def test_pref_normal(self):
        string = '1 2 2 3 2 5 5 9 9 7 7 6 7 8 9 10'
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(prefix(tree, 5), [5, 2, 1, 3, 9, 7, 6, 8, 10])

    def test_post_normal(self):
        string = '1 2 2 3 2 5 5 9 9 7 7 6 7 8 9 10'
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(postfix(tree, 5), [1, 3, 2, 6, 8, 7, 10, 9, 5])

    def test_pref_empty_tree(self):
        string = ''
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(prefix(tree, None), None)

    def test_pref_one_element_tree(self):
        string = '1'
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(prefix(tree, 1), [1])

    def test_post_empty_tree(self):
        string = ''
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(postfix(tree, None), None)

    def test_post_one_element_tree(self):
        string = '1'
        edges = makeEdges(string)
        tree = make_graph(edges)
        self.assertEqual(postfix(tree, 1), [1])

