def shutting_yard(string):
    string = string.split()
    op = {'+': 0, '-': 0, '*': 1, '/': 1, '**': 2}
    stack = []
    queue = []
    for item in string:
        if item.isdigit():
            queue.append(item)
        if item == '(':
            stack.append(item)
        if item == ')':
            while stack != []:
                if stack[-1] == '(':
                    stack.pop()
                    break
                queue.append(stack.pop())
            else:
                raise Exception('error')
        if item in op:
            if stack == [] or stack[-1] == '(':
               stack.append(item)
            elif op[stack[-1]] < op[item]:
                stack.append(item)
            else:
                while stack != [] and stack[-1] != '(' and (op[stack[-1]] > op[item] or (stack[-1] != '**' and op[stack[-1]] == op[item])):
                    queue.append(stack.pop())
                stack.append(item)
    if len(stack) != 0:
        for i in range(len(stack)):
            a = stack.pop()
            if a == '(':
                raise Exception('error')
            queue.append(a)

    return ' '.join(queue)


if __name__ == '__main__':
    string = ') )'
    print(shutting_yard(string))