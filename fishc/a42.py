class Nstr(str):
    def __sub__(self, other):
        return self.replace(other, '')

    def __lshift__(self, other):
        return self[other:] + self[:other]

    def __rshift__(self, other):
        return self[-other:] + self[:-other]


str1 = Nstr('woshinibaba')
str2 = Nstr('baba')

print(str1 - str2)
print(str1 << 3)
print(str1 >> 3)
