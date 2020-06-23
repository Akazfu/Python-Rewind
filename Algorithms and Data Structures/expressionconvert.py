from stack import Stack

prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}


def infix2postfix(infixexpr):
    opstack = Stack()
    postfix_list = []
    tokenlist = list(infixexpr.replace(' ', ''))
    for token in tokenlist:
        if token not in prec.keys() and token != ')':
            postfix_list.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = opstack.pop()
        else:
            while (not opstack.isEmpty()
                   and prec[opstack.peek()] >= prec[token]):
                postfix_list.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())
    return ''.join(postfix_list)


def evalpostfix(postfixexpr):
    nums = Stack()
    tokenlist = list(postfixexpr.replace(' ', ''))
    for token in tokenlist:
        if token not in prec.keys():
            nums.push(token)
        else:
            right = nums.pop()
            left = nums.pop()
            expression = left+token+right
            result = eval(expression)
            nums.push(str(result))
    if nums.size() == 1:
        return nums.pop()


if __name__ == "__main__":
    while True:
        infixexpr = input('Input a infix expression: ')
        print('Postfix expression is: ', end='')
        postfixexpr = infix2postfix(infixexpr)
        print(postfixexpr)
        print('result is ', evalpostfix('postfixexpr'))
