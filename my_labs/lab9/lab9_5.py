from sys import stdin


def makeEdges(s):
    # превращаем строку в список лексем с помощью split
    if s == '':
        return []
    lst = s.split()
    if len(lst) == 1:
        return [int(lst[0])]
    # создаем пустой список ребер
    edges = []
    # бежим по лексемам с шагом 2 и создаем ребра
    for i in range(1, len(lst), 2):
        edges.append((int(lst[i - 1]), int(lst[i])))

    return edges

def make_graph(edges):
    dict = {}
    if edges == []:
        return dict
    if len(edges) == 1 and isinstance(edges[0], int):
        dict[edges[0]] = None
        return dict

    for edge in edges:
        if edge[0] not in dict:
            dict[edge[0]] = [edge[1]]
            dict[edge[1]] = [edge[0]]
        else:
            dict[edge[0]].append(edge[1])
            if edge[1] in dict:
                dict[edge[1]].append(edge[0])
            else:
                dict[edge[1]] = [edge[0]]
    return dict

def prefix(tree, root, lst=None):
    if tree == {}:
        return ''
    if len(tree) == 1 and tree[root] == None:
        return [root]
    if lst == None:
        lst = []
    if root not in lst:
        lst.append(root)
    for v in tree[root]:
        if v not in lst:
            prefix(tree, v, lst)
    return lst

def postfix(tree, root, root_prev= None, lst=None,):
    if tree == {}:
        return ''
    if len(tree) == 1 and tree[root] == None:
        return [root]
    if lst == None:
        lst = []
    for v in tree[root]:
        if v != root_prev:
            postfix(tree, v, root, lst)
    if root not in lst:
        lst.append(root)
    return lst


if __name__ == '__main__':
    root = int(input())
    string = []
    for i in stdin:
        if i == '\n':
            break
        string.append(i.rstrip('\n'))
    string = ' '.join(string)
    string = makeEdges(string)
    tree = make_graph(string)
    pref = prefix(tree, root)
    post = postfix(tree, root)
    print(' '.join(map(str, pref)))
    print(' '.join(map(str, post)))
