# import sys
# if __name__ == "__main__":
#     height_xiaoming, n = map(lambda i: int(i), sys.stdin.readline().split())
#     height_friends = [int(i) for i in sys.stdin.readline().split()]
#     difference = []
#     result = []
#     for friend in height_friends:
#         difference.append(abs(friend - height_xiaoming))

#     zipped = zip(difference, height_friends)
#     sorted_zipped = sorted(zipped, key=lambda x:(x[0]))
#     unzip = zip(*sorted_zipped)
#     output_list = list([i for i in unzip][1])
#     output_list = [str(i)+' ' for i in output_list]
#     output = ''.join(output_list)
#     print(output)


import sys
if __name__ == "__main__":
    list1 = [int(i) for i in sys.stdin.readline().split()]
    list2 = [int(i) for i in sys.stdin.readline().split()]
    pairs = int(sys.stdin.readline())

    len1 = list1.pop(0)
    len2 = list2.pop(0)

    num2, num1 = divmod(pairs, len1)
    list1.sort()
    list2.sort()
    result = []

    

    for i in range(num2):
        for j in range(len1):
            result.append(list2[i])
            result.append(list1[j])

    if num2 >= len2:
        num2 = len2-1

    for k in range(num1):·
        result.append(list2[num2])
        result.append(list1[k])
    print(sum(result))
