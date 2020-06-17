def findfriend(num_kids, kids):
    print(kids)
    friends = [0] * num_kids
    kids = [int(i) for i in kids]
    for idx, kid in enumerate(kids):
        for i in range(idx+1, num_kids):
            if kids[i] > kid:
                friends[idx] = i
                break
    for i in friends:
        print(i, end=' ')


num_kids = int(input())
kids = input().split()
findfriend(num_kids, kids)
