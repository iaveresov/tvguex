def quickSort3Way(A, left = 0, right = None, verbose = False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1
        if left >= right:
            print(' '.join(map(str, A)))

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return A

    # инициализируем всевозможные указатели
    lt = left
    gt = right
    v = A[left]
    i = left
    # производим трехпутевое разбиение за один проход в соответствии с алгоритмом
    while i <= gt:
        if A[i] < v:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > v:
            A[gt], A[i] = A[i], A[gt]
            gt -= 1
        elif A[i] == v:
            i += 1


    # печатаем массив в нужном формате
    Ast = list(map(str, A))
    if verbose:
        if lt - 1 < left:
           Ast[lt] =  '[] ' + Ast[lt]
        else:
            Ast[left] = '[' + Ast[left]
            Ast[lt - 1] = Ast[lt - 1] + ']'
        if gt + 1 > right:
            if gt + 1 <= len(Ast) - 1:
                Ast[gt] +=' []'
            else:
                Ast.append('[]')
        else:
            Ast[right] = Ast[right] + ']'
            Ast[gt + 1] = '[' + Ast[gt + 1]
        print(' '.join(Ast))
    else:
        print(' '.join(Ast))
    # рекурсивно сортируем обе части (кроме той, что равна опорному элементу!)
    quickSort3Way(A, left, lt - 1, verbose)
    quickSort3Way(A, gt + 1, right, verbose)


# читаем список A (и возможно слово 'verbose' на второй строке)
A = list(map(int, input().split()))
try:
    verbose = input()
    if verbose == 'verbose':
        verbose = True
except EOFError:
    verbose = False
# вызываем quickSort3Way
quickSort3Way(A, verbose=verbose)