class MyQueue:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self):
        self.mas = [None] * 10
        self.head = 0
        self.tail = -1
        self.full = False


    def __str__(self):
        return str(self.mas)


    # метод добавления элемента в очередь
    def enqueue(self, x):
        if (self.tail + 1) % 10 == self.head and self.tail != -1:
            self.full = True
            return False
        self.tail = (self.tail + 1) % 10
        self.mas[self.tail] = x
        return True


    # метод удаления элемента из очереди
    def dequeue(self):
        self.full = False
        if self.head == (self.tail + 1) % 10 and self.full == False:
            return None
        a = self.mas[self.head]
        self.mas[self.head] = None
        self.head = (self.head + 1) % 10
        return a

    # метод для определения, пуста ли очередь
    def isEmpty(self):
        if self.full == False and (self.head - 1) % 10 == self.tail:
            return True
        return False

# Этот код менять не нужно. При корректной реализации класса MyQueue он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
"""
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
"""
A = MyQueue()
for i in range(10):
    A.enqueue(i)
for i in range(9):
    A.dequeue()
    print(A)
