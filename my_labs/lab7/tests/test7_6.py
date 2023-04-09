import unittest
from my_labs.lab7.lab7_6 import Item
from my_labs.lab7.lab7_6 import MyList


class Test_my_list1(unittest.TestCase):
    def test_str(self):
        A = MyList()
        self.assertEqual(str(A), '[]')
        A.append(1)
        A.append(2)
        A.append(3)
        A.append(4)
        self.assertEqual(str(A), '[1, 2, 3, 4]')
    def test_append(self):
        A = MyList()
        A.append(1)
        A.append(2)
        self.assertEqual(str(A), '[1, 2]')

    def test_pop(self):
        A = MyList()
        with self.assertRaises(RuntimeError) as e:
            A.pop()
        A.append(1)
        A.append(2)
        A.append(10)
        self.assertEqual(A.pop(), 10)
        self.assertEqual(str(A), '[1, 2]')

    def test_first_pop(self):
        A = MyList()
        with self.assertRaises(RuntimeError) as e:
            A.popFirst()
        A.append(1)
        A.append(2)
        A.append(3)
        self.assertEqual(A.popFirst(), 1)
        self.assertEqual(str(A), '[2, 3]')
        self.assertEqual(A.popFirst(), 2)
        self.assertEqual(str(A), '[3]')


    def test_len(self):
        A = MyList()
        for i in range(100):
            A.append(i)
        self.assertEqual(len(A), 100)

    def test_push_first(self):
        A = MyList()
        A.append(0)
        for i in range(1, 10):
            A.pushFirst(i)
        self.assertEqual(str(A),'[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]')