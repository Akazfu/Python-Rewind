def intsum(num_sum, count):
    differences = [i for i in range(count)]
    total = sum(differences)
    new_sum = num_sum - total

    if new_sum % count == 0:
        base = new_sum // count
        output = [base] * count

        for i in range(1, count):
            output[i] += differences[i]
        for o in output:
            print(o, end=' ')
    else:
        print('-1')


usr_input = input().split()
num_sum, count = int(usr_input[0]), int(usr_input[1])
intsum(num_sum, count)
