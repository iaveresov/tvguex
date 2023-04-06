def interpolSearch(A, elem):
    hi = len(A) - 1
    # если искомый элемент за границами диапазона,то делать нечего
    if elem  < A[0] or elem > A[hi]:
        return None

    # определим верхнюю границу и вызовем рекурсивную функцию
    return interpolSearchRec(A, elem, 0, hi)

def interpolSearchRec(A, elem, lo, hi, string=None):
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if string == None:
        string = []
    if lo > hi or elem < A[lo] or elem > A[hi]:
        return ' '.join(string)

    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if A[hi] == A[lo]:
        mid = lo
    # иначе - вычисляем mid по формуле
    else:
        mid = lo + round((elem - A[lo]) * ((hi - lo) / (A[hi] - A[lo])))

    # выполняем сравнение и рекурсивный вызов на одной из частей
    if elem == A[mid]:
        string.append(str(A[mid]))
        return ' '.join(string)
    if elem < A[mid]:
        string.append(str(A[mid]))
        return interpolSearchRec(A, elem, lo, mid - 1, string)
    else:
        string.append(str(A[mid]))
        return interpolSearchRec(A, elem, mid + 1, hi, string)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    print(interpolSearch(A, elem))
