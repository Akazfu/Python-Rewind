i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{i}*{j}={j * i}', end='  ')
        j += 1
    print()
    i += 1
