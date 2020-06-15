class Matrix:

    def __init__(self, l=0, w=0):
        self.__length = l
        self.__width = w

    def setRect(self, x, y):
        self.__length = x
        self.__width = y

    def getRect(self):
        return self.__length, self.__width

    def getArea(self):
        return self.__length * self.__width


x = Matrix()
# print(x.__length)
print(x.getArea())
x.setRect(5, 6)
print(x.getArea())
