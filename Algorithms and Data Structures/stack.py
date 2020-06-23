class Stack:
    def __init__(self, list_=[]):
        self.list = list_

    def push(self, item):
        self.list.append((item))

    def pop(self, idx=-1):
        return self.list.pop(idx)

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []
