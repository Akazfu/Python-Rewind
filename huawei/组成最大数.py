input_str = '4589,101,41425,9999'
list_str = input_str.split(',')

for i in range(len(list_str)):
    for j in range(i+1, len(list_str)):
        if (int(list_str[i]+list_str[j])
                < int(list_str[j]+list_str[i])):
            list_str[i], list_str[j] = (list_str[j], list_str[i])
print(''.join(list_str))
