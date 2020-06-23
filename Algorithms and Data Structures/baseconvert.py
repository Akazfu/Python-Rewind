def tostr(n, base):
    covertstring = '0123456789ABCDEF'
    if n < base:
        return covertstring[n]
    else:
        return tostr(n//base, base) + covertstring[n % base]


print(tostr(1453, 16))
