# -*- coding: utf-8 -*-
import random
from datastructures import Queue


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(num_seconds, pages_perminute):
    lab_printer = Printer(pages_perminute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            print(current_second)
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            print('cs', current_second)
            print('ts', next_task.time_stamp)
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    print(waiting_times)
    average_wait = sum(waiting_times)/len(waiting_times)
    print("Average wait %6.2f secs %3d tasks remaining."
          % (average_wait, print_queue.size()))


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.time_stamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.time_stamp


if __name__ == "__main__":
    for i in range(10):
        simulation(3600, 10)
