from typing import Any

# большую часть методов можно скопировать из упражнения 10.4
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
    # этот метод необходимо модифицировать, добавив в него эвристику сжатия путей
    def root(self, x: int) -> int:
        if x == self._id[x]:
            return x
        self._id[x]: int = self.root(self._id[x])
        return self._id[x]

    # возвращает строку с элементами множества
    # этот метод необходимо модифицировать, добавив в него печать массива rank
    def __str__(self) -> str:
        return ' '.join(list(map(str, self._id))) + '\n' + ' '.join(list(map(str, self._rank)))


    # объединяет два множества, представленные своими элементами x и y
    # этот метод необходимо модифицировать, добавив в него эвристику ранга
    def union_set(self, x: int, y: int) -> None:
        root_x: int = self.root(x)
        root_y: int = self.root(y)
        if root_y == root_x:
            return
        if self._rank[root_x] < self._rank[root_y]:
            self._id[root_x]: int = root_y
        else:
            self._id[root_y]: int = root_x
            if self._rank[root_x] == self._rank[root_y]:
                self._rank[root_x]: int = self._rank[root_x] + 1

    # возвращает True, если x и y связаны, и False в противном случае
    def connected(self, x: int, y: int) -> bool:
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
            line: list[str, ...] = line.split()
            op: str
            x: Any
            y: Any
            op, x, y = line
            x, y = int(x), int(y)
            if op == '+':
                uf.union_set(x, y)
            elif op == '?':
                print(uf.connected(x, y))
    except:
        pass