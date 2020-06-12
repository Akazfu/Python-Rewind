def findflower(x):
    c = x % 10
    b = (x // 10) % 10
    a = x // 100
    if x == a**3 + b**3 + c**3:
        print(x)


for i in range(100, 1000):
    findflower(i)
