# coding=utf-8
import sys


def shortestpath(map):
    mom, baby, obsticles = [], [], []
    for i in range(n):
        for j in range(n):
            if map_[i][j] == '-3':
                mom = [i, j]
            elif map_[i][j] == '-2':
                baby = [i, j]
            elif map_[i][j] == '-1':
                obsticles.append([i, j])


def findneighbour(i, j):
    neighbour_list = [[]*n]
    if map_[i+1][j+1]: 
    if map_[i+1][j-1]: 
    if map_[i-1][j+1]: 
    if map_[i-1][j-1]: 



n = int(sys.stdin.readline())
map_ = list()
for _ in range(n):
    map_.append(sys.stdin.readline().split())
shortestpath(map_)
