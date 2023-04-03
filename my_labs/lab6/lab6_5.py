def partition(A, left, right):
    # инициализируем два указателя
    i = left + 1
    j = right

    # если разбивать нечего, то выходим
    if i > j:
        return j
    if i == j:
        if A[left] < A[j]:
            return left
        if A[left] >= A[j]:
            A[j], A[left] = A[left], A[j]
            return j
    # запускаем внешний цикл, который будет работать, пока указатели двигаются навстречу
    while i <= j:
        # перемещаем вперед указатель i (не забываем про границу массива!)
        while i <= right and A[i] < A[left]:
            i += 1
        # перемещаем назад указатель j (не забываем про границу массива!)
        while j > left and A[j] > A[left]:
            j -= 1

        # делаем проверки согласно алгоритму, меняем значения местами и двигаем указатели
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    # после цикла i указывает на первый элемент второй группы, j - на последний элемент первой
    # ставим опорный элемент на нужное место и возвращаем его позицию
    A[left], A[j] = A[j], A[left]
    return j


def quickSort(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
        if left >= right:
            print(' '.join(map(str, A)))

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return A

    # производим разбиение с помощью partition
    p = partition(A, left, right)
    # печатаем массив
    Ast = list(map(str, A))
    if verbose:
        if p - 1 < left:
           Ast[p] =  '[] ' + Ast[p]
        else:
            Ast[left] = '[' + Ast[left]
            Ast[p - 1] = Ast[p - 1] + ']'
        if p + 1 > right:
            if p + 1 <= len(Ast) - 1:
                Ast[p] +=' []'
            else:
                Ast.append('[]')
        else:
            Ast[right] = Ast[right] + ']'
            Ast[p + 1] = '[' + Ast[p + 1]
        print(' '.join(Ast))
    else:
        print(' '.join(Ast))
    # рекурсивно сортируем обе части

    quickSort(A, left, p - 1, verbose)
    quickSort(A, p + 1, right, verbose)


# читаем список A (и возможно слово 'verbose' на второй строке)
if __name__ == '__main__':
    A = list(map(int, input().split()))
    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False
    # вызываем quickSort
    quickSort(A, verbose= verbose)


