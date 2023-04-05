def binSearch(A, elem):
    if A == []:
        return None
    hi = len(A) - 1
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[hi]:
        return None


    # определим верхнюю границу и вызовем рекурсивную функцию
    return binSearchRec(A, elem, 0, hi)

def binSearchRec(A, elem, lo, hi, string=None):
    # если подмассив пустой, то делать нечего
    if string == None:
        string = []

    if lo > hi:
        return ' '.join(string)
    # определяем средний элемент
    mid = (lo + hi) // 2
    # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] == elem:
        string.append(str(A[mid]))
        return ' '.join(string)
    if A[mid] > elem:
        string.append(str(A[mid]))
        return binSearchRec(A, elem, lo, mid - 1, string)
    else:
        string.append(str(A[mid]))
        return binSearchRec(A, elem, mid + 1, hi, string)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    print(binSearch(A, elem))