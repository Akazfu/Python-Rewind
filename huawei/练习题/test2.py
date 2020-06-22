# coding=utf-8
import sys
import math


def getkth(n, k):
    k -= 1
    # 1,2,3
    nums = [str(i+1) for i in range(n)]
    result = ''
    while n != 0:
        n -= 1
        factorial = math.factorial(n)
        quo, mod = divmod(k, factorial)
        result += nums.pop(quo)
        k = mod
    return(result)


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
print(getkth(n, k))
