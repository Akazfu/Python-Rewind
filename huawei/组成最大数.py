import math


def findmax(input_str):
    input_str = input_str.replace(' ', '')
    list_str = input_str.split(',')
    print(list_str)

    for i in range(len(list_str)):
        for j in range(i+1, len(list_str)):
            if (int(list_str[i]+list_str[j])
                    < int(list_str[j]+list_str[i])):
                list_str[i], list_str[j] = (list_str[j], list_str[i])
    print(list_str)
    result = ''.join(list_str)
    print(result)


input_str = '1015,101,9,91,98,98'
findmax(input_str)
