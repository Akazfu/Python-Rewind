# i = 0

# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)

# while else break后 bool为True 不执行else 语句

i = 1

while i <= 3:
    ans = input('please input -->')
    if ans == 'bingo':
        print('true')
        break
    else:
        print(f'false, {3-i} times to go ')
    i += 1
else:
    print('game over')
