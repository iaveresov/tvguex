class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.mas = [None] * 10
        self.head = 0
        self.tail = -1
        self.lenght = 10
        self.empty = True

    def __str__(self):
        return str(self.mas)


    # метод добавления элемента в очередь
    def enqueue(self, x):
        if not self.empty and (self.head - self.tail) % self.lenght == 1:
            return False
        self.empty = False
        self.tail = (self.tail + 1) % 10
        self.mas[self.tail] = x
        return True


    # метод удаления элемента из очереди
    def dequeue(self):
        if self.empty and (self.head - self.tail) % self.lenght == 1:
            return None
        a = self.mas[self.head]
        self.mas[self.head] = None
        self.head = (self.head + 1) % 10
        if (self.head - self.tail) % self.lenght == 1:
            self.empty = True
        return a

    # метод для определения, пуста ли очередь
    def isEmpty(self):
        return self.empty


# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    A = MyQueue()
    print(A.isEmpty())
    A.enqueue(1)
    A.enqueue(2)
    print(A.dequeue())
    A.enqueue(3)
    print(A.dequeue())
    A.enqueue(4)
    A.enqueue(5)
    print(A.isEmpty())
    A.enqueue(6)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.isEmpty())
    A.enqueue(10)
    A.enqueue(11)
    A.enqueue(12)
    A.enqueue(13)
    A.enqueue(14)
    A.enqueue(15)
    A.enqueue(16)
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())
    print(A.dequeue())