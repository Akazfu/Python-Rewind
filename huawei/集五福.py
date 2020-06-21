input_ = '11000,00111,11111,00011,10000,00001,00001'
input_list = [i for i in input_.split(',')]
count = [0, 0, 0, 0, 0]
for person in input_list:
    for i in range(len(person)):
        if person[i] == '1':
            count[i] += 1

print(min(count))
