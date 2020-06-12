while 1:
    usr_in = input('input the text--> ')
    with open('user_input.txt', 'a') as f:
        f.write(usr_in+'\n')
