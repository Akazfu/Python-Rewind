class Ticket:
    def __init__(self, week_date='1', age='18'):
        self.__age = age
        self.__week_date = week_date
        self.__price = 100.0

    def getPrice(self):
        if self.__week_date in '67':
            self.__price *= 1.2

        if (int(self.__age) < 18):
            self.__price *= 0.5

        return self.__price


# Daren = Ticket()
# print(Daren.getPrice())
# Xiaohai = Ticket(age='4')
# print(Xiaohai.getPrice())
# Daren_6 = Ticket('6', '38')
# Xiaohai_7 = Ticket('7', '16')
# print(Daren_6.getPrice())
# print(Xiaohai_7.getPrice())
