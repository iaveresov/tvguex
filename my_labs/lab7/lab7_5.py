def insertMas2Mas(A, n, i, B):
    k = len(B)
    # если вставлять уже некуда, пишем full
    if len(A) - n < k:
        print('full')
        return

    # в цикле печатаем переносы элементов
    print()
    for j in reversed(range(i, n)):
        A[j + k] = A[j]
        print(f'A[{j + k}] = A[{j}]')

    # в цикле печатаем копирование элементов из B в нужные места
    for j in range(i, i + k):
        A[j] = B[j - i]
        print(f'A[{j}] = {B[j - i]}')

if __name__ == '__main__':
    args = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input()))
    insertMas2Mas(A, *args, B)