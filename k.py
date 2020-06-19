import sys
if __name__ == "__main__":
    # list1 = [int(i) for i in sys.stdin.readline().split()]
    # list2 = [int(i) for i in sys.stdin.readline().split()]
    # pairs = int(sys.stdin.readline())

    # list1 = [5, 1, 2, 3, 4, 5]
    # list2 = [3, 1, 1, 2]
    # pairs = 2
    list1 = [9, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [3, 1, 2, 3]
    pairs = 20
    # list1 = [3, 1, 1, 2]
    # list2 = [3, 1, 2, 3]
    # pairs = 2
    len1 = list1.pop(0)
    len2 = list2.pop(0)
    print(list1)
    print(list2)

    num2, num1 = divmod(pairs, len1)
    print(num2, num1)
    result = []

    for i in range(num2):
        for j in range(len1):
            result.append(list2[i])
            result.append(list1[j])

    for k in range(num1):
        result.append(list2[num2])
        result.append(list1[k])
        
    print(result)    
    print(sum(result))