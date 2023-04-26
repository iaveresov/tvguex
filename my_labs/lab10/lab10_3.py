

# большую часть методов можно скопировать из упражнения 10.2
# не забудьте про аннотирование типов!
class UnionFind:
    _id: list[int, ...]
    _size: list[int, ...]
    # конструктор, создающий пустые массивы для СНМ и весовой эвристики
    def __init__(self):
        self._id = []
        self._size = []

    # добавляет в СНМ еще один элемент
    # не забудьте про вес нового элемента!
    def make_set(self) -> None:
        self._id.append(len(self._id))
        self._size.append(1)
    # возвращает корень дерева, которому принадлежит x
    def root(self, x: int) -> int:
        while x != self._id[x]:
            x = self._id[x]
        return x

    # возвращает строку с элементами множества
    # этот метод необходимо модифицировать, добавив в него печать массива size
    def __str__(self) -> str:
        return  ' '.join(list(map(str, self._id))) + '\n' +  ' '.join(list(map(str, self._size)))
    # объединяет два множества, представленные своими элементами x и y
    # этот метод необходимо модифицировать, добавив в него весовую эвристику
    def union_set(self, x: int, y: int) -> None:
        x_root: int = self.root(x)
        y_root: int = self.root(y)
        if x_root == y_root:
            return
        if self._size[x_root] < self._size[y_root]:
            self._id[x_root] = y_root
            self._size[y_root] = self._size[y_root] + self._size[x_root]
        else:
            self._id[y_root] = x_root
            self._size[x_root] = self._size[y_root] + self._size[x_root]

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