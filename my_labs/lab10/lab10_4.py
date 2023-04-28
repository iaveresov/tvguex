from typing import Any
# большую часть методов можно скопировать из упражнения 10.2
# не забудьте про аннотирование типов!
class UnionFind:
    _id: list[int, ...]
    _rank: list[int, ...]
    # конструктор, создающий пустые массивы для СНМ и эвристики ранга
    def __init__(self) -> None:
        self._id = []
        self._rank = []

    # добавляет в СНМ еще один элемент
    # не забудьте про ранг нового элемента!
    def make_set(self) -> None:
        self._id.append(len(self._id))
        self._rank.append(0)

    # возвращает корень дерева, которому принадлежит x
    def root(self, x) -> int:
        curr: int = x
        while curr != self._id[curr]:
            curr: int = self._id[curr]
        return curr

    # возвращает строку с элементами множества
    # этот метод необходимо модифицировать, добавив в него печать массива rank
    def __str__(self) -> str:
        return ' '.join(str(x) for x in self._id) + '\n' + ' '.join(str(x) for x in self._rank)

    # объединяет два множества, представленные своими элементами x и y
    # этот метод необходимо модифицировать, добавив в него эвристику ранга
    def union_set(self, x: int, y: int) -> None:
        x_root: int = self.root(x)
        y_root: int = self.root(y)
        if x_root == y_root:
            return
        if self._rank[x_root] < self._rank[y_root]:
            self._id[x_root]: int = y_root
        else:
            self._id[y_root] = x_root
            if self._rank[x_root] == self._rank[y_root]:
                self._rank[x_root] += 1

    # возвращает True, если x и y связаны, и False в противном случае
    def connected(self, x, y) -> bool:
        return self.root(x) == self.root(y)

if __name__ == '__main__':

    # считайте N
    N: int = int(input())

    # создайте СНМ и положите в нее N элементов с помощью make_set
    uf: UnionFind = UnionFind()
    for elem in range(N):
        uf.make_set()

    # следующая конструкция позволит вам считывать данные из файла, пока они есть
    try:
        while True:
            # считайте команду, определите ее тип и выполните ее, вызвав соответствующий метод uf
            line: str = input()
            if line == 'print':
                print(uf)
                continue
            op: str
            x: Any
            y: Any
            op, x, y = line.split()
            x, y = int(x), int(y)
            if op == '+':
                uf.union_set(x, y)
            elif op == '?':
                print(uf.connected(x, y))
    except:
        pass