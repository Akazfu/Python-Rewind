# coding=utf-8
import sys


def getaverageweight(str_input):
    str_list = str_input.split()
    total_weight = 0

    for i in str_list:
        total_weight += len(i)

    average_weight = total_weight / len(str_list)
    return average_weight


str_input = sys.stdin.readline()
print('%.2f' % getaverageweight(str_input))
