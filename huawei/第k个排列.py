import math


def kth_outcome(n, k):
    list_n = [i for i in range(1, n+1)]
    result = ''
    k = k-1

    while n > 0:
        n -= 1
        factorial = math.factorial(n)
        quotient = k // factorial
        mod = k % factorial
        k = mod
        result += str(list_n.pop(quotient))
    print(result)


n = int(input())
k = int(input())
kth_outcome(n, k)
