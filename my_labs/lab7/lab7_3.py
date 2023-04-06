def fibSearch(A, elem):
    n = len(A)
    # если искомый элемент за границами диапазона,то делать нечего
    if n == 0:
        return None
    if elem < A[0] or elem > A[n - 1]:
        return None

    # вычисляем нужное число Фибоначчи
    fKm2 = 0
    fKm1 = 1
    fK = 0
    while fK < n:
        fK = fKm1 + fKm2
        if fK >= n:
            break
        fKm2 = fKm1
        fKm1 = fK
    # вызываем рекурсивную функцию
    return fibSearchRec(A, elem, 0, fKm1, fK, n)

def fibSearchRec(A, elem, lo, fKm1, fK, n, string= None):
    if string == None:
        string = []
    # если подмассив пустой ИЛИ из одного элемента, который не равен elem, то делать нечего
    if fK == 0 or (fK == 1 and A[lo] != elem):
        string.append(str(A[lo]))
        return ' '.join(string)
    # если подмассив из одного элемента, который равен elem, то возвращаем ответ и завершаемся
    if fK == 1 and elem == A[lo]:
        string.append(str(A[lo]))
        return ' '.join(string)

    # вычисляем (k-2)-е число Фибоначчи
    fKm2 = fK - fKm1

    # вычисляем mid - правый элемент первого подмассива (смотрим, чтобы он не выпал за границы)
    mid = min(lo + fKm2 - 1, n - 1)
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        string.append(str(A[mid]))
        return ' '.join(string)
    if elem < A[mid]:
        string.append(str(A[mid]))
        return fibSearchRec(A, elem, lo, fKm1 - fKm2, fKm2, n, string)
    else:
        string.append(str(A[mid]))
        return fibSearchRec(A, elem, lo + fKm2, fKm2, fKm1, n, string)

if __name__ == '__main__':
    elem = int(input())
    A = list(map(int, input().split()))
    print(fibSearch(A, elem))