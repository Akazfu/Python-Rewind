def guessage(n):
    if n == 1:
        return 10
    else: 
        return guessage(n-1) + 2

print(guessage(5))