k = 525
s = 6
sum_difference = 0
result = []

for i in range(s):
    sum_difference += i

if (k - sum_difference) % s == 0:
    k1 = (k - sum_difference) // s
    for i in range(s):
        result.append(str(k1+i))
    print(' '.join(result))
else:
    print(-1)
