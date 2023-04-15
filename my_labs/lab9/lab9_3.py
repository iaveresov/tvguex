from io import IOBase
from sys import stdin

def edges2lists(N, edges):
    lists = [[] for i in range(N)]
    for edge in edges:
        if edge[1] not in lists[edge[0]]:
            lists[edge[0]].append(edge[1])
        if edge[0] not in lists[edge[1]]:
            lists[edge[1]].append(edge[0])
    return lists

def makeEdges(s):
    # превращаем строку в список лексем с помощью split
    lst = s.split()

    # создаем пустой список ребер
    edges = []

    # бежим по лексемам с шагом 2 и создаем ребра
    for i in range(1, len(lst), 2):
        edges.append((int(lst[i - 1]), int(lst[i])))

    return edges

def print_lists(lists):
    for item in lists:
        string = ' '.join(list(map(str, item)))
        print(string)


if __name__ == '__main__':
    N = input()
    string = []
    for i in stdin:
        if i == '\n':
            break
        string.append(i.rstrip('\n'))
    string = ' '.join(string)
    edges = makeEdges(string)
    lists = edges2lists(N, edges)
    print_lists(lists)