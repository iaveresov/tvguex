import unittest
from my_labs.lab9.lab9_4 import shutting_yard
from my_labs.lab9.lab9_8 import Node
from my_labs.lab9.lab9_8 import parse_tree
from my_labs.lab9.lab9_8 import main


class Test_tree(unittest.TestCase):
    def test_tree1(self):
        self.assertEqual(str(main('2 + 3 * 4 - 5')), '(- (+ (2 () ()) (* (3 () ()) (4 () ()))) (5 () ()))')


    def test_one_element(self):
        self.assertEqual(str(main('2')), '(2 () ())')


    def test_empty_tree(self):
        self.assertEqual(str(main('')), '()')

    def test_two_elements(self):
        self.assertEqual(str(main('2 + 3')), '(+ (2 () ()) (3 () ()))')


    def test_tree2(self):
        self.assertEqual(str(main('( 2 + 3 ) + 4')), '(+ (+ (2 () ()) (3 () ())) (4 () ()))')