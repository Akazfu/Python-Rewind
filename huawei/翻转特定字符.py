input_str = 'aA1bB2cC3 1'
list_str, mode = list(input_str.split()[0]), input_str.split()[1]
out, flip = [], []

if mode == '1':
    for i in range(len(list_str)):
        if list_str[i].islower():
            flip.append(list_str[i])
            list_str[i] = '\t'
elif mode == '2':
    for i in range(len(list_str)):
        if list_str[i].isupper():
            flip.append(list_str[i])
            list_str[i] = '\t'
elif mode == '3':
    for i in range(len(list_str)):
        if list_str[i].isnumeric():
            flip.append(list_str[i])
            list_str[i] = '\t'

for i in range(len(list_str)):
    if list_str[i] == '\t':
        list_str[i] = flip.pop()

print(''.join(list_str))
