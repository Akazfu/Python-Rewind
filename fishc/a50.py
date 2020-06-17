import sys


class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            print('常量已经存在')
        elif not name.isupper():
            print('常量名得是大写')
        self.__dict__[name] = value


sys.modules[__name__] = Const()
