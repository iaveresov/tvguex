def insert2Mas(A, n, i, elem):
    # если вставлять уже некуда, пишем full
    if n == len(A):
        print('full')
        return

    # в цикле печатаем переносы элементов
    for j in reversed(range(i, n)):
        A[j + 1] = A[i]
        print(f'A[{j + 1}] = A[{j}]')

    # печатаем копирование элемента elem в нужное место
    print('A[{}] = {}'.format(i, elem))

args = list(map(int, input().split()))
A = list(map(int, input().split()))
insert2Mas(A, *args)
