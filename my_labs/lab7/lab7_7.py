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


    def get_head(self):
        return self.head


    def get_tail(self):
        return self.tail

    def set_tail(self, tail):
        self.tail = tail

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

    # реализуйте метод, добавляющий новый элемент со значением x после p. Помните об указателе tail!
    def addAfter(self, p, x):
        if p == None:
            raise Exception('Некуда вставлять')
        if p.get_next() == None:
            x = Item(data=x)
            self.tail.set_next(x)
            x.set_prev(self.tail)
            self.tail = x
        else:
            x = Item(data=x)
            next = p.get_next()
            x.set_next(next)
            next.set_prev(x)
            p.set_next(x)
            x.set_prev(p)


    # реализуйте метод удаления элемента p. Также помните об указателе tail! Он не должен "съехать"
    def remove(self, p):
        if self.head.get_next() == None:
            raise Exception
        prev = p.get_prev()
        next = p.get_next()
        if next == None:
            prev.set_next(None)
            self.tail = prev
        else:
            prev.set_next(next)
            next.set_prev(prev)

    def find(self, x):
        a = self.head.get_next()
        while a != None:
            if a.get_data() == x:
                return a
            a = a.get_next()
        return None


    # реализуйте перегрузку индексации на чтение
    def __getitem__(self, idx):
        if idx >= self.__len__() or idx < 0 or self.__len__() == 0:
            raise Exception('Неверно задан индекс')
        a = self.head.get_next()
        num = 0
        while a != None:
            if idx == num:
                return a.get_data()
            num += 1
            a = a.get_next()


    # реализуйте перегрузку индексации на запись
    def __setitem__(self, idx, x):
        if idx >= self.__len__() or idx < 0 or self.__len__() == 0:
            raise Exception('Неверно задан индекс')
        a = self.head.get_next()
        num = 0
        while a != None:
            if idx == num:
                a.set_data(x)
                return
            num += 1
            a = a.get_next()

    # реализуйте перегрузку метода in (может можно воспользоваться уже реализованным find?)
    def __contains__(self, item):
        if self.find(item) != None:
            return True
        return False


    # реализуйте сложение двух списков (попробуйте использовать уже написанные методы для упрощения кода)
    def __add__(self, other):
        new_lst = MyList()
        item_self = self.head.get_next()
        item_other = other.get_head().get_next()
        while item_self != None:
            new_lst.append(item_self.get_data())
            item_self = item_self.get_next()

        while item_other != None:
            new_lst.append(item_other.get_data())
            item_other = item_other.get_next()
        return  new_lst


    # реализуйте метод конкатенации двух списков. Второй список не забудьте "обнулить"
    def concat(self, other):
        item_other = other.get_head().get_next()
        while item_other != None:
            self.append(item_other.get_data())
            item_other = item_other.get_next()
        other.get_head().set_next(None)
        other.set_tail(other.get_head())


    # метод, возвращающий итератор, мы написали за вас. Вам осталось только дописать сам класс итератора
    def __iter__(self):
        return MyListIterator(self.head.get_next())

class MyListIterator:
    def __init__(self, item):
       self.currentItem = item

    def __next__(self):
        if self.currentItem == None:
            raise StopIteration
        returned = self.currentItem
        self.currentItem = self.currentItem.get_next()
        return returned
        # здесь необходимо написать код, который вернет значение
        # элемента, на который ссылается currentItem, и передвинет его
        # на следующий элемент. Если currentItem никуда не ссылается
        # (т.е. равен None), то необходимо выбросить исключение
        # raise StopIteration


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
    if (1 in A):
        print("True")
    else:
        print("False")
    if (2 in A):
        print("True")
    else:
        print("False")
    for i in range(6,10):
        A.append(i)
    A[0] = 0
    A[4] = -1
    for i in range(len(A)):
        print(A[i])
    for i in A:
        print(i)
    A.remove(A.find(-1))
    print(A)
    B = MyList()
    for i in range(6):
        B.append(i)
    A = A + B
    A.append(100)
    B[0] = 100
    print(A)
    print(B)
    A.concat(B)
    A.append(100)
    print(A)
    print(B)
