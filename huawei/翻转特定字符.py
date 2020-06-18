def flipstr(input_str, mode):
    list_str = list(input_str)
    flip_list = []
    print(list_str)

    if mode == '1':
        for i in range(len(list_str)):
            if list_str[i].islower():
                flip_list.append(list_str[i])
                list_str[i] = '\t'

    elif mode == '2':
        for i in range(len(list_str)):
            if list_str[i].isupper():
                flip_list.append(list_str[i])
                list_str[i] = '\t'
    elif mode == '3':
        for i in range(len(list_str)):
            if list_str[i].isnumeric():
                flip_list.append(list_str[i])
                list_str[i] = '\t'

    flip_list.reverse()
    for i in range(len(list_str)):
        if list_str[i] == '\t':
            list_str[i] = flip_list.pop(0)
    print(list_str)


input_str = 'aAbB2cC3'
mode = '3'
flipstr(input_str, mode)
