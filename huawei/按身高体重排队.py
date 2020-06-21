n = '3'
height = '90 110 90'
weight = '45 60 45'

n = int(n)
height = [int(i) for i in height.split()]
weight = [int(i) for i in weight.split()]
id_ = [i for i in range(1, n+1)]
zip_ = zip(id_, height, weight)
id_list = [str(x)+' ' for x, _, _ in sorted(
    zip_, key=lambda x: (x[1], x[2], x[0]))]

print(''.join(id_list))
