num_kids = 8
kids = [123, 124, 125, 121, 119, 122, 126, 123]
friends = ['0'] * num_kids

for idx, kid in enumerate(kids):
    for i in range(idx+1, num_kids):
        if kids[i] > kid:
            friends[idx] = str(i)
            break
print(' '.join(friends))
