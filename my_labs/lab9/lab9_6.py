def dfs_post(v, matrix, lst=None, string = None):
    if lst is None:
        lst = []
    if string is None:
        string = []
    lst.append(v)
    for i in range(len(matrix[0])):
        if i not in lst and matrix[v][i] == 1:
            dfs_post(i, matrix, lst, string)
    string.append(v)
    return string

def dfs_pref(v, matrix, lst=None, string = None):
    if lst is None:
        lst = []
    if string is None:
        string = []
    lst.append(v)
    string.append(v)
    for i in range(len(matrix[0])):
        if i not in lst and matrix[v][i] == 1:
            dfs_pref(i, matrix, lst, string)
    return string

if __name__ == '__main__':
    matrix = []
    param = list(map(int, input().split()))
    v = param[0]
    N = param[1]
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    pref = dfs_pref(v, matrix)
    post = dfs_post(v, matrix)
    print(' '.join(list(map(str, pref))))
    print(' '.join(list(map(str, post))))