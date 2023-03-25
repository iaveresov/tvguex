def merge(A, left, mid, right):
    # вспомогательный массив, в который будут сливаться элементы
    AUX = []

    # список, в который мы будем записывать порядок сливания элементов
    indexes = []

    # Инициализируем указатели i и j
    i = left
    j = mid + 1

    # Цикл, осуществляющий слияние
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            AUX.append(A[i])
            indexes.append(i)
            i += 1
        else:
            AUX.append(A[j])
            indexes.append(j)
            j += 1

            # Дописываем хвост (почитайте справку к функции extend для списков) и не забываем про indexes
    AUX.extend(A[i: mid + 1])
    AUX.extend(A[j: right + 1])
    indexes.extend(range(i, mid + 1))
    indexes.extend(range(j, right + 1))
    # Возвращаем назад в массив A результат нашей работы (обратите внимание на присваивание срезу!)
    A[left:right + 1] = AUX

# читаем массив A, массив B, склеиваем их
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A = A1 + A2

# вызываем merge, результат преобразуем к нужному виду и выводим
ans = merge(A, 0, len(A1) - 1, len(A) - 1)
print(' '.join(list(map(str, A))))
print(' '.join(map(str, ans)))