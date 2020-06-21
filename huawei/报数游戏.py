m = 4
list_ = [i for i in range(1, 101)]
count = 1

if m < 1 or m > 100:
    print('ERROR!')
else:
    while len(list_) >= m:
        for i in list_:
            if count == m:
                list_.pop(0)
                count = 1
            else:
                list_.append(list_.pop(0))
                count += 1
list_.sort()
list_ = [str(i) for i in list_]
print(','.join(list_))
