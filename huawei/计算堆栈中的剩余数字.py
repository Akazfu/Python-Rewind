array = [1, 1, 2, 3, 5, 8]
stack = []

for item in array:
    print(item)
    sums = []
    if len(stack) != 0:
        for i in range(len(stack)):
            sums.insert(0, sum(stack[i:]))
        print(sums)
        if item in sums:
            for i in range(sums.index(item)+1):
                stack.pop()
            stack.append(item*2)
        else:
            stack.append(item)
    else:
        stack.append(item)
for i in range(len(stack)):
    print(str(stack.pop()), end=' ')
