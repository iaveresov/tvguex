def count_sort(A):
    if len(A) <= 1:
        return
    maxim = max(A)
    c = [0] * (maxim + 1)
    for i in range(len(A)):
        c[A[i]] += 1
    res = []
    for i in range(maxim + 1):
        res += [i] * c[i]
    A[:] = res
    if __name__ == '__main__':
        print(' '.join(list(map(str, A))))


if __name__ == '__main__':
    count_sort(list(map(int, input().split())))
