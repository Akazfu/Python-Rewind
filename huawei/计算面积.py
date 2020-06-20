import sys
list_input = sys.stdin.readline().split()
n, e = map(int, list_input)
instruction, graph = [], []
current, area = 0, 0

for i in range(n):
    instruction.append(sys.stdin.readline().split())

for i in range(e):
    graph.append([i, 0])

for i in range(e):
    for j in instruction:
        if graph[i][0] == int(j[0]):
            current += int(j[1])
    graph[i][1] += current

area_list = [i[1] for i in graph]
area = sum(area_list)
print(area)
