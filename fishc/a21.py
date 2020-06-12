def power(x, y):
    if y == 1:
        return x
    else:
        return x * power(x, y-1)

list_input = list(map(int, input().split()))
print(power(list_input[0], list_input[1]))