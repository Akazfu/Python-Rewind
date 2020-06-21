import math
n = 5
k = 72
k = k - 1
nums = [i for i in range(1, n+1)]
result = ''

while n > 0:
    n -= 1
    factorial = math.factorial(n)
    quo, mod = divmod(k, factorial)
    result += str(nums.pop(quo))
    k = mod
print(result)
