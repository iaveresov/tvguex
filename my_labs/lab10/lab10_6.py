
# для метода sift_up понадобится вспомогательный метод parent
# не забудьте про аннотирование типов!
def parent(p: int) -> int:
    # возвращаем индекс родителя элемента p (не забудьте про сложности округления
    # и целочисленного деления в Питоне! протестируйте свой метод!)
    return max(0, round((p - 1) // 2))


def shift_up(heap: list[int, ... ], p: int) -> None:
    current: int = p
    # если мы в корне, то выходим
    if current == 0:
        return
    prnt: int = parent(current)
    # пока мы не в корне и текущий элемент меньше родительского, меняем их и поднимаемся выше
    while heap[prnt] > heap[current]:
        heap[prnt]: int
        heap[current]: int
        heap[prnt], heap[current] = heap[current], heap[prnt]
        current: int = prnt
        prnt: int = parent(current)


if __name__ == '__main__':
    # считать массив heap
    heap: list[int, ...] = list(map(int, input().split()))

    # считать индекс всплываемого элемента
    p: int = int(input())

    # осуществляем всплытие
    shift_up(heap, p)

    # напечатать heap
    print(' '.join(list(map(str, heap))))