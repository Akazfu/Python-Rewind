class Matrix:
    length = 0
    width = 0

    def setRect(self, x, y):
        self.length = x
        self.width = y

    def getRect(self):
        return self.length, self.width

    def getArea(self):
        return self.length * self.width
# x = Matrix()
# x.setRect(5, 6)
# print(x.getArea())
