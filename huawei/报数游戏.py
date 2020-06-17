def circlecount(m):
    m = int(m)
    people = [i for i in range(1, 101)]
    count = 0
    idx = 0
    while len(people) >= m:
        count += 1
        idx += 1
        if count == m:
            people.pop(idx)
            count = 0
    print(people)


m = 3
callout(m)
