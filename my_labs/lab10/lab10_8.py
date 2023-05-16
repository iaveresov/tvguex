# для метода sift_down понадобятся вспомогательные методы left_son, right_son, min_son
# не забудьте про аннотирование типов!
def left_son(p: int) -> int:
    # возвращаем индекс левого сына элемента p
    return 2 * p + 1


def right_son(p: int) -> int:
    # возвращаем индекс правого сына элемента p
    return 2 * p + 2


def min_son(p: int, heap: list[int, ...], lenght: int) -> int:
    # возвращаем индекс минимального сына элемента p или -1, если p - лист
    l: int = left_son(p)
    r: int = right_son(p)
    tail: int = lenght - 1
    if l > tail:
        return -1
    if l < tail and r <= tail:
        minim = min(heap[l], heap[r])
        if heap[l] == minim:
            return l
        else:
            return r
    elif l == tail:
        return l

def sift_down(heap: list[int, ...], p: int) -> None:
    lenght: int = len(heap)
    minCh: int = min_son(p, heap, lenght)
    # пока мы не в листе и текущий элемент больше минимального из сыновей,
    # меняем их местами и погружаемся ниже
    while minCh > 0 and heap[minCh] < heap[p]:
        heap[minCh], heap[p] = heap[p], heap[minCh]
        p: int = minCh
        minCh: int = min_son(p, heap, lenght)


if __name__ == '__main__':
    # считать массив heap
    heap: list[int, ...] = list(map(int, input().split()))

    # считать индекс всплываемого элемента
    p: int = int(input())

    # осуществляем всплытие
    sift_down(heap, p)

    # напечатать heap
    print(' '.join(list(map(str, heap))))