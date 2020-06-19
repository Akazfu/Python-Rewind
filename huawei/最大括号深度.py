def checkbracket(input_str):
    left = {'(', '[', '{'}
    right = {')', ']', '}'}
    check = []
    count, deep = 0, 0

    if (input_str[0] not in left) or (input_str[-1] not in right):
        return 0

    for cha in input_str:
        if cha in left:
            check.append(cha)
            count += 1

        elif cha == ')':
            if check.pop() == '(':
                if count > deep:
                    deep = count
                count = 0
            else:
                return 0

        elif cha == ']':
            if check.pop() == '[':
                if count > deep:
                    deep = count
                count = 0
            else:
                return 0

        elif cha == '}':
            if check.pop() == '{':
                if count > deep:
                    deep = count
                count = 0
            else:
                return 0

        else:
            return 0

    return deep


while True:
    try:
        input_str = input()
        print(checkbracket(input_str))

    except:
        print(0)
