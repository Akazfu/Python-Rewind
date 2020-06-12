def pow(x, y):
    total = x
    for i in range (y-1):
        total *= x
    return total

str_list = input().split()
print(str_list)
x = int(str_list[0])
y = int(str_list[1])

print(pow(x, y))
