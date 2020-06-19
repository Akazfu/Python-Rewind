import time


def monkeyclimb(steps):
    if steps == 1:
        return 1
    elif steps == 2:
        return 1
    elif steps == 3:
        return 2
    else:
        return monkeyclimb(steps-1) + monkeyclimb(steps-3)


def monkeyclimb_loop(steps):
    if steps == 1:
        return 1
    elif steps == 2:
        return 1
    elif steps == 3:
        return 2
    ways = [1, 1, 2]
    for i in range(3, steps):
        ways.append(ways[i-1] + ways[i-3])
    return ways[steps-1]


while True:
    steps = int(input())
    print('')
    start = time.time()
    print(monkeyclimb_loop(steps))
    stop = time.time()
    print(f'Time cost loop is {stop - start}')
    start = time.time()
    print(monkeyclimb(steps))
    stop = time.time()
    print(f'Time cost recursion is {stop - start}')
