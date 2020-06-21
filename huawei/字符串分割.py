input_str = '12abc-abCABc-4aB@'
k = 3
head_idx = input_str.find('-')
head = input_str[:head_idx]
tail = input_str[head_idx+1:]
tail = tail.replace('-', '')
tail_list = []
for i in range(0, len(tail), k):
    count_lower = 0
    count_upper = 0
    for cha in tail[i:i+k]:
        if cha.islower():
            count_lower += 1
        elif cha.isupper():
            count_upper += 1
    if count_lower > count_upper:
        tail_list.append('-'+tail[i:i+k].lower())
    elif count_lower < count_upper:
        tail_list.append('-'+tail[i:i+k].upper())
    else:
        tail_list.append('-'+tail[i:i+k])
print(head+''.join(tail_list))
