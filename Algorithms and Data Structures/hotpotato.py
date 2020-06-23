from datastructures import Queue


def hotpotate(namelist, num):
    queue = Queue()
    for name in namelist:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()


if __name__ == "__main__":
    namelist = ['a', 'b', 'c', 'd', 'e', 'f']
    print(hotpotate(namelist, 7))
