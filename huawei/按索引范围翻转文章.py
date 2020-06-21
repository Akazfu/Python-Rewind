usr_str = 'I   am a           developer.    '
start = int('0')
stop = int('2')

str_list = usr_str.split()
cut_list = []
new_list = []
cut_list = str_list[start:stop+1]
cut_list.reverse()
new_list = str_list[:start] + cut_list + str_list[stop+1:]
print(' '.join(new_list))
