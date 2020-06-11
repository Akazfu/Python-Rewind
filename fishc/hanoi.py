def hanoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n-1, x, z, y)
        print(x, '-->', z)
        hanoi(n-1, y, x, z)


while 1:
    n, x, y, z = input('Please input values >>> ').split()
    hanoi(int(n), x, y, z)
