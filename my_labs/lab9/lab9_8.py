from typing import  Optional, Union
from my_labs.lab9.lab9_4 import shutting_yard

class Node:
    data: Optional[str]
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        if self.data is None:
            return '()'
        if self.left is None:
            return f'({self.data} () ())'
        if self.right is None:
            return '()'
        return f'({self.data} {str(self.right)} {str(self.left)})'


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

def main(string):
    ops = shutting_yard(string)
    tree = parse_tree(ops)
    return tree


if __name__ == '__main__':
    string = input()
    print(main(string))




