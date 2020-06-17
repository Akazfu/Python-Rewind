def strflip(usr_str, start, stop):
    str_list = usr_str.split()
    cut_list = []
    new_list = []
    for i in range(start, stop+1):
        cut_list.append(str_list[i])
    while cut_list:
        new_list.append(cut_list.pop())
    cut_list = str_list[:start] + new_list + str_list[stop+1:]
    index = 1
    for i in range(1, len(cut_list)):
        cut_list.insert(index, ' ')
        index += 2
    new_str = ''.join(cut_list)
    print(new_str)


usr_str = input()
start = int(input())
stop = int(input())
strflip(usr_str, start, stop)

# I am a developer.
