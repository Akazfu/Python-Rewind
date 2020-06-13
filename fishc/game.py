''' 用Python设计的一个小游戏'''

import random

seed = random.getstate()
target = random.randint(1, 9)
i = 0
with open('seed.txt', 'w') as f:
    f.write(str(seed))

while i < 3:
    try:
        temp = input('1-9哪个数字？')
        guess = int(temp)
    except (ValueError, KeyboardInterrupt, EOFError) as reason:
        print('\n出错了！ '+str(reason))
        break
    if guess == target:
        print('对了。')
        break
    elif guess <= target:
        print('小了')
        print(f'还剩下{2-i}次机会')
    elif guess >= target:
        print('大了')
        print(f'还剩下{2-i}次机会')
    i += 1
else:
    print('游戏结束了。')
