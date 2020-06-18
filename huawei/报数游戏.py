def circlecount(m):
    m = int(m)
    people = [str(i) for i in range(1, 101)]
    count = 0
    index = -1
    while len(people) >= m:
        count += 1
        if count == m:
            people.pop(0)
            count = 0
        else:
            people.append(people.pop(0))

    people.sort()
    for i in range(len(people)-1):
        people[i] = people[i] + ','
    result = ''.join(people)
    print(result)


m = 3
circlecount(m)
