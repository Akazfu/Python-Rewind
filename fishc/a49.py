'''
0 return或者异常
1 可以挂起函数，暂停到当前时间节点
2 可以 next
3 return改成yeild
4 迭代
5 死循环用来持续输出yeild
'''


def generev(data):
    for index in range(-1, -len(data)-1, -1):
        yield data[index]


g = generev([0, 1, 2, 4, 5, 6, 4, 3, 2, 3432, 3])

try:
    while True:
        print(next(g))
except StopIteration as identifier:
    pass
