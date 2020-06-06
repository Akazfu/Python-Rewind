import math


def find_max(numbers):
    max_num = -math.inf
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num


