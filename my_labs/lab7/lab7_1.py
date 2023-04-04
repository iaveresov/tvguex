def binSearch(A, elem):
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[len(A) - 1]:
        return None
    # определим верхнюю границу и вызовем рекурсивную функцию
    hi = len(A) - 1
    return binSearchRec(A, elem, 0, hi)

def binSearchRec(A, elem, lo, hi, string=[]):
    # если подмассив пустой, то делать нечего
    mid = (lo + hi) // 2
    if lo > hi:
        string.append(A[mid])
    # определяем средний элемент

    # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] == elem:
        string.append(str(A[mid]))
        return ' '.join(string)
    if A[mid] > elem:
        string.append(str(A[mid]))
        return binSearchRec(A, mid, hi, string)
    else:
        string.append(str(A[mid]))
        return binSearchRec(A, elem, lo, mid - 1, string)


A = [0, 2, 3, 8, 9, 10, 11, 14, 23, 28]
print(binSearch(A, 11))