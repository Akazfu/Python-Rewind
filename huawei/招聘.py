schedule = ['1 2', '2 3', '3 4', '4 5', '5 6', '1 2', '2 3', '3 4', '4 5']
m = 2
n = 9
slots = []
added = False
for i in range(n):
    added = False
    if len(slots) == 0:
        slots.append([schedule[i]])
    else:
        for hr in slots:
            if len(hr) < m:
                if schedule[i] not in hr:
                    hr.append(schedule[i])
                    added = True
        if not added:
            slots.append([schedule[i]])
print(slots)
print(len(slots))
