def lucky_five(group):
    count = [0, 0, 0, 0, 0]
    group_list = group.split(',')

    for member in group_list:
        for inx, val in enumerate(member):
            if val == '1':
                count[inx] += 1
    print(count)
    print(min(count))


usr_input = input()
lucky_five(usr_input)
