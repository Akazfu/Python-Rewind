import sys
if __name__ == "__main__":
    array = [int(i) for i in sys.stdin.readline().split()]
    stack = []

    for item in array:
        sums = []
        if len(stack) != 0:
            for i in range(len(stack)):
                sums.insert(0, sum(stack[i:]))
            if item in sums:
                for i in range(sums.index(item)+1):
                    stack.pop()
                stack.append(item*2)
            else:
                stack.append(item)
        else:
            stack.append(item)
        print(item)
        print(stack)
        print(sums)

    for i in range(len(stack)):
        print(str(stack.pop()), end=' ')