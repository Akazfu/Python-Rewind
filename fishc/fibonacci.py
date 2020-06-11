import time

def fabo(x):
    if x <= 2:
        return 1
    else:
        return fabo(x-1) + fabo(x-2)


def fabo_loop(x):
    n1 = 1
    n2 = 1
    n3 = 1

    while x > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        x -= 1

    return n3


while 1:
    x = input('input a number: ')

    start_time = time.time()   
    print(fabo(int(x)))
    end_time = time.time()             
    run_time = end_time - start_time   
    print('run_time: ', run_time)

    start_time = time.time()
    print(fabo_loop(int(x)))
    end_time = time.time()             
    run_time = end_time - start_time   
    print('run_time: ', run_time)
