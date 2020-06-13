import math


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.length = math.sqrt((p1.x - p2.x) ** 2 +
                                (p1.y - p2.y) ** 2)

    def get_length(self):
        return self.length


p1 = Point(1, 1)
p2 = Point(5, 5)
l1 = Line(p1, p2)
print(l1.get_length())
