import time


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


steps = int(input())
print(monkeyclimb_loop(steps))
