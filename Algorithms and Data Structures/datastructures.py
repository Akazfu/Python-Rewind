class Stack:
    def __init__(self, list_=[]):
        self.list = list_

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop(-1)

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []


class Queue:
    def __init__(self, list_=[]):
        self.list = list_

    def enqueue(self, item):
        self.list.append(item)

    def dequeue(self):
        return self.list.pop(0)

    def peek(self):
        return self.list[0]

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []


class Deque:
    def __init__(self, list_=[]):
        self.list = list_

    def addfront(self, item):
        self.list.insert(0, item)

    def addrear(self, item):
        self.list.append(item)

    def removefront(self):
        return self.list.pop(0)

    def removerear(self):
        return self.list.pop(-1)

    def size(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()

        if previous is None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


class OrderedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getdata() > item:
                stop = True
            else:
                previous = current
                current = current.getnext()
        temp = Node(item)
        if previous is None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()

        if previous is None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
