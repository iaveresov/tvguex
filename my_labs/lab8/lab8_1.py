class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V=None, E=None):
        
    # метод конструирования строкового представления графа
    # def __str__ ...

    # метод добавления метки вершине или ребру
    # def __setitem__ ...

    # метод возврата метки вершины или ребра
    # def __getitem__ ...

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self):


    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    # def add_edge ...

    # генератор или итератор, перечисляющий все рёбра графа
    # def edges ...

    # генератор или итератор, перечисляющий все вершины графа
    # def vertices ...

    # генератор или итератор, перечисляющий все рёбра, выходящие из вершины v
    # def outgoing ...

    pass


# Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
"""
g = Graph()
g.add_vertex("u")
g.add_vertex("v")
g.add_vertex("w")
g.add_edge(("u", "v"))
g.add_edge(("u", "w"))
g.add_edge(("v", "w"))
print(g)
print(list(g.vertices()))
print(list(g.edges()))
print(list(g.outgoing("u")))
print(list(g.outgoing("w")))
g["u"] = 1
g[("u", "v")] = 42
print(g["v"])
print(g["u"])
print(g[("u", "v")])
print(g[("v", "w")])
g2 = Graph(["a", "b"], [("a", "b"), ("b", "a")])
print(g2)
"""