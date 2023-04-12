import unittest
from my_labs.lab7.lab7_7 import Item
from my_labs.lab7.lab7_7 import MyList

class Test_my_list(unittest.TestCase):

    def test_add_after(self):
        A = MyList()
        A.append(1)
        A.append(2)
        A.append(3)
        A.addAfter(A.find(2), 10)
        self.assertEqual(str(A), '[1, 2, 10, 3]')

    def test_remove(self):
        A = MyList()
        with self.assertRaises(Exception) as e:
            A.remove(1)
        A.append(1)
        A.append(2)
        A.append(3)
        A.remove(A.find(2))
        self.assertEqual(str(A), '[1, 3]')
        self.assertEqual(str(A.get_tail()), '3')

    def test_find(self):
        A = MyList()
        self.assertEqual(A.find(1), None)
        for i in range(12):
            A.append(i)
        self.assertEqual(str(A.find(11)), '11')
        self.assertEqual(str(A.find(13)), 'None')


    def test_getitem(self):
        A = MyList()
        with self.assertRaises(Exception) as e:
            a = A[0]
        for i in range(14):
            A.append(i)
        self.assertEqual(A[10], 10)

    def test_setitem(self):
        A = MyList()
        with self.assertRaises(Exception) as e:
            A[0] = 1
        for i in range(21):
            A.append(i)
        self.assertEqual(A[10], 10)

    def test_contains_(self):
        A = MyList()
        self.assertFalse(1 in A)
        for i in range(24):
            A.append(i)
        self.assertTrue(12 in A)


    def test_add(self):
        A = MyList()
        B = MyList()
        for i in range(4):
            A.append(i)
        for i in range(5):
            B.append(i * 10)
        C = A + B
        self.assertEqual(str(C), '[0, 1, 2, 3, 0, 10, 20, 30, 40]')

    def test_concat(self):
        A = MyList()
        B = MyList()
        for i in range(4):
            A.append(i)
        for i in range(5):
            B.append(i * 10)
        A.concat(B)

        self.assertEqual(str(A), '[0, 1, 2, 3, 0, 10, 20, 30, 40]')
        self.assertEqual(str(B), '[]')

    def test_iter(self):
        A = MyList()
        for i in range(10):
            A.append(i)
        lst = []
        for i in range(10):
            lst.append(A[i])
        self.assertEqual(lst, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])