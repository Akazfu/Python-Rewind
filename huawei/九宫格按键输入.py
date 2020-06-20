usr_input = '#2222/220999/9443#123321//#1133222/222'
usr_input += '/'
dict9 = {'1': [',', '.'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'j'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
         '0': [' ']}
output = []
mode = 1
buffer = -1
count = 0

for cha in usr_input:
    if cha == '#':
        mode *= -1
        count = 0
        buffer = -1
    else:
        if mode == 1:
            if cha != '/':
                output.append(cha)
        elif mode == -1:
            if cha in dict9.keys():
                if buffer == -1:
                    buffer = cha
                    count += 1
                else:
                    if cha == buffer:
                        count += 1
                    else:
                        while count > len(dict9[buffer]):
                            count -= len(dict9[buffer])
                        output.append(dict9[buffer][count-1])
                        buffer = cha
                        count = 1
            elif cha == '/':
                while count > len(dict9[buffer]):
                    count -= len(dict9[buffer])
                output.append(dict9[buffer][count-1])
                buffer = -1
                count = 0

print(''.join(output))
