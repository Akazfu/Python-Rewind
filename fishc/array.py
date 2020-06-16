class CountList:
    def __init__(self, *args):
        self.list = [x for x in args]
        self.count = {}.fromkeys(range(len(self.list)), 0)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        return self.count[key]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __delitem__(self, key):
        self.list.pop(key)


x = CountList(1, 2, 3, 4, 5)
print(x.list)
print(len(x))
x[0] = 666
print(x.list)
del x[0]
print(x.list)
