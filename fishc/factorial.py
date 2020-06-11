def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

def factorial_loop(x):
    fac = 1
    for i in range (1, x+1):
        fac = fac * i
    return fac

while 1:
    x = int(input('input number: '))
    print(factorial(x))
    print(factorial_loop(x))