class MyDes:
    def __init__(self, value=0, owner=0):
        self.value = value
        self.owner = owner

    def __get__(self, instance, owner):
        print('正在获取变量：', self.owner)
        return self.value

    def __set__(self, instance, value):
        print("正在修改变量：", self.owner)
        self.value = value

    def __delete__(self, instance):
        print("正在删除变量：", self.owner)
        print('这个变量没法删除。')


class Test:
    x = MyDes(10, 'x')


# if __name__ == "__main__":
#     test = Test()
#     y = test.x
#     y
#     test.x = 8
#     del test.x
#     test.x
