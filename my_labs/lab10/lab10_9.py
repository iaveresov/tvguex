from typing import Optional


# не забудьте про аннотирование типов!
class Heap:
    heap: list[int, ...]
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self) -> None:
        self.heap = []

    def left_son(self, p: int) -> int:
      # возвращаем индекс левого сына элемента p
        return 2 * p + 1

    def right_son(self, p: int) -> int:
        # возвращаем индекс правого сына элемента p
        return 2 * p + 2

    def parent(self, p: int) -> int:
        # возвращаем индекс родителя элемента p (не забудьте про сложности округления
        # и целочисленного деления в Питоне! протестируйте свой метод!)
        return max(0, round((p - 1) // 2))

    def min_son(self, p: int, lenght=None) -> int:
        # возвращаем индекс минимального сына элемента p или -1, если p - лист
        lenght = len(self.heap)
        l: int = self.left_son(p)
        r: int = self.right_son(p)
        tail: int = lenght - 1
        if l > tail:
            return -1
        if l < tail and r <= tail:
            minim = min(self.heap[l], self.heap[r])
            if self.heap[l] == minim:
                return l
            else:
                return r
        elif l == tail:
            return l

    def sift_up(self, p: int) -> None:
        current: int = p
        # если мы в корне, то выходим
        if current == 0:
            return
        prnt: int = self.parent(current)
        # пока мы не в корне и текущий элемент меньше родительского, меняем их и поднимаемся выше
        while self.heap[prnt] > self.heap[current]:
            self.heap[prnt]: int
            self.heap[current]: int
            self.heap[prnt], self.heap[current] = self.heap[current], self.heap[prnt]
            current: int = prnt
            prnt: int = self.parent(current)

    def sift_down(self, p: int) -> None:
        lenght: int = len(self.heap)
        minCh: int = self.min_son(p, lenght)
        # пока мы не в листе и текущий элемент больше минимального из сыновей,
        # меняем их местами и погружаемся ниже
        while minCh > 0 and self.heap[minCh] < self.heap[p]:
            self.heap[minCh], self.heap[p] = self.heap[p], self.heap[minCh]
            p: int = minCh
            minCh: int = self.min_son(p, lenght)

   # метод для добавления элемента x в кучу
    def add(self, x):
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

   # метод для возврата минимума
    def min(self) -> int:
        return self.heap[0]

   # метод для возврата минимума и удаления его из кучи
    def get_min(self) -> Optional[int]:
        if len(self.heap) == 0:
            return
        if len(self.heap) == 1:
            ret: int = self.heap.pop()
            return ret
        ret: int = self.heap[0]
        a: int = self.heap.pop()
        self.heap[0]: int = a
        self.sift_down(0)
        return ret
   # печать массива с бинарным деревом кучи
    def __str__(self) -> str:
        return ' '.join(map(str, self.heap))
# Этот код менять не нужно. При корректной реализации класса Heap он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

heap = Heap()
heap.add(1)
heap.add(10)
heap.add(8)
heap.add(32)
heap.add(11)
heap.add(38)
heap.add(42)
heap.add(78)
heap.add(31)
print(heap)