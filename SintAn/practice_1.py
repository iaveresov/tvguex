class SA:
    def __init__(self):
        self.inp = ""
        self.i = 0
        self.len = 0
        self.result = True
        self.opz = []
        self.digit = {"0","1","2","3","4","5","6","7","8","9"}
        self.stack = []

    def get_opz(self):
        return self.opz

    def expr(self):
        if not(self.term()) : return False
        if not(self.elist()) : return False

        return True

    def term(self):
        if not(self.factor()) : return False
        if not(self.tlist()) : return False
        return True

    def elist(self):
        if self.i >= self.len: return True
        if self.inp[self.i] == "+":
            self.i += 1
            if not(self.term()) : return False
            self.opz.append('+')
            if not(self.elist()) : return False

            return True

        elif self.inp[self.i] == "-":
            self.i += 1
            if not (self.term()): return False
            self.opz.append('-')
            if not (self.elist()): return False

        return True

    def tlist(self):
        if self.i >= self.len: return True
        if self.inp[self.i] == "*":
            self.i += 1
            if not (self.factor()): return False
            self.opz.append('*')
            if not (self.tlist()): return False

            return True

        elif self.inp[self.i] == "/":
            self.i += 1
            if not (self.factor()): return False
            self.opz.append('/')
            if not (self.tlist()): return False
        return True

    def factor(self):
        if self.i >= self.len: return False
        if self.inp[self.i] == "(":
            self.i += 1
            if not(self.expr()): return False
            if (self.i < self.len) and self.inp[self.i] == ")":
                self.i += 1
            else: return False
            return True
        elif self.inp[self.i] in self.digit:
            self.opz.append(self.inp[int(self.i)])
            self.i += 1
            return True
        else: return False

    def pars(self, inp):
        self.inp = inp
        self.len = len(inp)
        self.result = self.expr()


def make_operation(stack, operation):
    try:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(operation(op2, op1))
    except:
           return 'error'

# определим функцию, которая будет делать всю работу
def calculate_ops(ops):
    # в качестве стека будем использовать обычный питоновский список
    stack = []
    # перебираем все элементы ops и вычисляем значение в соответствии с алгоритмом
    for item in ops:
        if item.isdigit():
            stack.append(int(item))
        else:
            {'+': lambda: make_operation(stack, lambda a, b: a + b),
             '-': lambda: make_operation(stack, lambda a, b: a - b),
             '*': lambda: make_operation(stack, lambda a, b: a * b),
             '/': lambda: make_operation(stack, lambda a, b: a // b),
             '**': lambda: make_operation(stack, lambda a, b: a ** b)
             }[item]()

    # после того, как все прочитано, на стеке должно быть ровно одно значение - результат
    # если это так, то возвращаем его, иначе возвращаем ошибку
    if len(stack) == 1:
        return stack[0]
    else:
        return 'error'

# считываем строку и делим ее на лексемы
sa = SA()
sa.pars('(2+3)*(5-2)')

# вычисляем результат и печатаем его
print(calculate_ops(sa.get_opz()))