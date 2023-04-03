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
        while A[i] < A[left] and i <= right:
            i +=  1
        # перемещаем назад указатель j (не забываем про границу массива!)
        while A[j] > A[left] and j > left:
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

# читаем left, right, массив A
ind = list(map(int, input().split()))
A = list(map(int, input().split()))
# вызываем partition и выводим результат
j = partition(A, *ind)
print(' '.join(list(map(str, A))))
print(j)