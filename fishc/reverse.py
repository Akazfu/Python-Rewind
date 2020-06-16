class MyRev:
    def __init__(self, *args):
        self.list = [i for i in args]
        self.index = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1

        return self.list[self.index]


r = MyRev(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(r.list)
for i in r:
    print(i)
