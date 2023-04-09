class Item:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


    def get_next(self):
        return self.next


    def get_prev(self):
        return self.prev


    def get_data(self):
        return self.data


    def set_next(self, next):
        self.next = next


    def set_prev(self, prev):
        self.prev = prev


    def set_data(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


class MyList:
    # конструктор, который корректно инициализирует голову и хвост списка
    def __init__(self):
        self.head = Item()
        self.tail = self.head

    # метод добавления элемента в конец списка
    def append(self, x):
        x = Item(data=x)
        if self.head.get_next() == None:
            self.head.set_next(x)
            x.set_prev(self.head)
            self.tail = x
        else:
            self.tail.set_next(x)
            x.set_prev(self.tail)
            self.tail = x

    # метод удаления элемента из конца списка (не забываем про пустой список!)
    def pop(self):
        if self.head.get_next() == None:
            raise RuntimeError('Список пуст')
        popped = self.tail.get_data()
        new_tail = self.tail.get_prev()
        new_tail.set_next(None)
        self.tail = new_tail
        return popped

    # метод добавления элемента в начало списка (помним про указатель tail!)
    def pushFirst(self, x):
        x  = Item(data=x)
        if self.head.get_next() == None:
            self.head.set_next(x)
            x.set_prev(self.head)
            self.tail = x
        else:
            first_elem = self.head.get_next()
            first_elem.set_prev(x)
            x.set_next(first_elem)
            x.set_prev(self.head)
            self.head.set_next(x)

    # метод удаления элемента из начала списка (опять не забываем про пустой список!)
    def popFirst(self):
        if self.head.get_next() == None:
            raise RuntimeError('Список пуст')
        popped = self.head.get_next()
        if popped.get_next() == None:
            self.tail = self.head
        else:
            self.head.set_next(popped.get_next())
        return popped.get_data()

    # метод определения длины списка
    def __len__(self):
        if self.head.get_next() == None:
            return 0
        else:
            lenght = 0
            a = self.head.get_next()
            while a != None:
                lenght += 1
                a = a.get_next()
            return lenght

    # метод конструирования строкового представления списка
    def __str__(self):
        if self.head.get_next() == None:
            return '[]'
        string = '['
        a = self.head.get_next()
        while a != None:
            if a.get_next() == None:
                string += str(a) + ']'
                break
            string += str(a)+ ',' + ' '
            a = a.get_next()
        return string

# Этот код менять не нужно. При корректной реализации класса MyList он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    A = MyList()
    A.append(1)
    A.pushFirst(3)
    A.append(5)
    A.append(1)
    A.pushFirst(5)
    print(A)
    print(A.popFirst())
    print(A.pop())
    print(A)
    print(len(A))
