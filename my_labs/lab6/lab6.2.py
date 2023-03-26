def merge(A, left, mid, right):
    # вспомогательный массив, в который будут сливаться элементы
    AUX = []
    # Инициализируем указатели i и j
    i = left
    j = mid + 1

    # Цикл, осуществляющий слияние
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            AUX.append(A[i])
            i += 1
        else:
            AUX.append(A[j])
            j += 1

    # Дописываем хвост (почитайте справку к функции extend для списков) и не забываем про indexes
    AUX.extend(A[i: mid + 1])
    AUX.extend(A[j: right + 1])
    # Возвращаем назад в массив A результат нашей работы (обратите внимание на присваивание срезу!)
    A[left:right + 1] = AUX

def mergeSort(A, left=0, right=None, verbose=False):
    #если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return A

    # определяем середину
    mid = (left + right) // 2

    # рекурсивно сортируем обе половины
    mergeSort(A, left, mid, verbose)
    mergeSort(A, mid + 1, right, verbose)
    # печатаем массив и производим слияние с помощью функции merge
    Ast = list(map(str, A))
    if verbose:
        for i in range(len(A)):
            if i == left:
                Ast[i] = '[' + Ast[i]
            if i == mid:
                Ast[i] = Ast[i] + ']'
            if i == mid + 1:
                Ast[i] = '[' + Ast[i]
            if i == right:
                Ast[i] = Ast[i] + ']'
    print(' '.join(Ast))
    merge(A, left, mid, right)

# читаем список A (и возможно слово 'verbose' на второй строке)
A = list(map(int, input().split()))
try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False

# вызываем mergeSort и не забываем напечатать результат его работы еще раз!
mergeSort(A, verbose= verbose)
print(' '.join(list(map(str, A))))
