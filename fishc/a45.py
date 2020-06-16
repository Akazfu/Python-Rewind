'''
0 设置属性 不对，无限递归
1 __getattribute__
2 '3' | '2' 'None'
3 '2''1'
4 recursion无限递归
'''


class Demo:
    def __init__(self, name='FishC'):
        self.x = name

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __getattr__(self, name):
        print("属性不存在")


demo = Demo()
print(demo.x)
demo.x = "X-man"
print(demo.x)
demo.z
