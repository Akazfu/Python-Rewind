class Stack:
    stack_count = 0

    def __init__(self, array):
        self.count = 0
        self.list = []
        for i in array:
            self.push(i)
        Stack.stack_count += 1

    def isEmpty(self):
        if self.count:
            return False
        else:
            return True

    def push(self, data):
        self.list.append(data)
        self.count += 1

    def pop(self):
        self.list.pop()
        self.count -= 1

    def top(self):
        return self.list[0]

    def bottom(self):
        return self.list[-1]

    def __del__(self):
        Stack.stack_count -= 1

# 理解类对象属性以及实例对象属性的区别，一般调用实例对象属性
