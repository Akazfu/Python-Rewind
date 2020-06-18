def uncompressed(input_str):
    if input_str.isalnum() and input_str.islower():
        list_str = list(input_str)
        multipler = ''
        legal_check = True

        if list_str[-1].isnumeric():
            print('!error')
            legal_check = False

        for i in range(len(list_str)):
            if list_str[i].isnumeric():
                multipler += list_str[i]
                list_str[i] = ''
            elif list_str[i].islower():
                if multipler != '':
                    multipler = int(multipler)
                    if int(multipler) > 2:
                        list_str[i] *= multipler
                        multipler = ''
                    else:
                        print('!error')
                        legal_check = False
                        break
    else:
        print('!error')
        legal_check = False

    if legal_check:
        print(''.join(list_str))


input_str = '100a3a'
uncompressed(input_str)
