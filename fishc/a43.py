class HowMany():
    def __init__(self, *args):
        self.count = 0
        for a in args:
            self.count += 1
        print(self.count)


c1 = HowMany('1', 4, 3, [1, 2, 3, 4], 4444)
