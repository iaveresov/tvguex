from typing import Union
from typing import Optional

# возможно какие-то методы можно скопировать из упражнения 10.1
# не забудьте про аннотирование типов!
class UnionFind:
    id: list[int, ...]
    # конструктор, создающий пустой массив для хранения СНМ
    def __init__(self):
        self.id = []

    # добавляет в СНМ еще один элемент
    def make_set(self):
        self.id.append(len(self.id))

    # возвращает корень дерева, которому принадлежит x
    def root(self, x: int):
        while x != self.id[x]:
            x = self.id[x]
        return x

    # возвращает строку с элементами множества
    def __str__(self):
        return ' '.join(list(map(str, self.id)))

    # объединяет два множества, представленные своими элементами x и y
    def union_set(self, y: int, x: int):
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:
            return
        self.id[x_root] = y_root

    # возвращает True, если x и y связаны, и False в противном случае
    def connected(self, x: int, y: int):
        return self.root(x) == self.root(y)

if __name__ == '__main__':
    # считайте N
    N: int = int(input())

    # создайте СНМ и положите в нее N элементов с помощью make_set
    uf = UnionFind()
    for elem in range(N):
        uf.make_set()

    # следующая конструкция позволит вам считывать данные из файла, пока они есть
    try:
        while True:
            # считайте команду, определите ее тип и выполните ее, вызвав соответствующий метод uf
            line = input()
            if line == 'print':
                print(uf)
            else:
                line = line.split()
                if line[0] == '+':
                    uf.union_set(int(line[1]), int(line[2]))
                if line[0] == '?':
                    print(uf.connected(int(line[1]), int(line[2])))
    except:
        pass