def fib(num):
    print("生成器已经执行 ")
    a = 0
    b = 1
    yield a
    yield b
    for i in range(2, num+1):
        a, b = b, a+b
        yield b


num = 200
f = fib(num)
for i in range(num):
    print(next(f), end=' ')
