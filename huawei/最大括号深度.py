input_str = '[][][][][]{}{{{{}}}}((([[[]]])))'
left = ['(', '[', '{']
right = [')', ']', '}']
stack = []
count, deep = 0, 0

if (input_str[0] not in left) or (input_str[-1] not in right):
    deep = 0
else:
    for cha in input_str:
        if cha in left:
            stack.append(cha)
            count += 1

        if cha in right:
            if right.index(cha) == left.index(stack.pop()):
                if count > deep:
                    deep = count
                count = 0
            else:
                deep = 0
                break
print(deep)
