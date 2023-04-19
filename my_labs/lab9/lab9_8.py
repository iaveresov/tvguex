from typing import  Optional, Union
from my_labs.lab9.lab9_4 import shutting_yard

class Node:
    data: Optional[str]
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        if self.left is None:
            self.left = '()'
        if self.right is None:
            self.right = '()'
        return f'({self.data} {self.right} {self.left})'


    def get_data(self):
        return self.data


    def get_left(self):
        return self.left


    def get_right(self):
        return self.right


    def set_left(self, left):
        self.left = left


    def set_right(self, right):
        self.right = right


def parse_tree(string: str) -> Node:
    string = string.split()
    stack: list[Node, ...]
    stack = []
    op = {'+', '-', '*', '/', '**'}
    for item in string:
        if item.isdigit():
            number = Node(item)
            stack.append(number)
        if item in op:
            oper = Node(item)
            v = stack.pop()
            u = stack.pop()
            oper.set_left(v)
            oper.set_right(u)
            stack.append(oper)
    if stack != []:
        return stack.pop()
    else:
        return Node(None)


def traversal(tree: Node) -> Union[list[str, ...], str]:
    if tree is None:
        return '()'
    if tree.get_data() is None:
        return '()'
    string = f'({tree.get_data()} {traversal(tree.get_left())} {traversal(tree.get_right())}'
    return string



if __name__ == '__main__':
    string = input()
    ops = shutting_yard(string)
    tree = parse_tree(ops)
    print(tree)




