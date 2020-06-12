# def min(list1):
#     minm = list1[0]
#     for i in list1:
#         if i < minm:
#             minm = i
#     return minm

# list1 = [5, 67, 90, -67, 110, 45, 156, -998]
# print(min(list1))

def sum(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result


print(sum([1, 2.1, 2.3, 'a', '1', True]))
