def make_operation(stack, operation):
    try:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(operation(op2, op1))
    except:
        raise Exception('error')

# определим функцию, которая будет делать всю работу
def calculate_ops(ops):
    ops = ops.split()
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
        raise Exception('error')

# считываем строку и делим ее на лексемы


# вычисляем результат и печатаем его
if __name__ == '__main__':
    ops = '12 21 + 1 1 - /'
    print(calculate_ops(ops))
