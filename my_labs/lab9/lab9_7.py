def BFS(v, matrix):
    string = []
    queue = []
    marked = []
    marked.append(v)
    queue.append(v)
    while queue != []:
        u = queue.pop(0)
        string.append(u)
        for x in range(len(matrix[0])):
            if x not in marked and matrix[u][x] == 1:
                marked.append(x)
                queue.append(x)
    return string

if __name__ == '__main__':
    matrix = []
    param = list(map(int, input().split()))
    v = param[0]
    N = param[1]
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    bfs = BFS(v, matrix)
    print(' '.join(list(map(str, bfs))))
