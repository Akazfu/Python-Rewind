def sort_weightheight(n, height, weight):
    height_list = [int(i) for i in height.split()]
    weight_list = [int(i) for i in weight.split()]
    idx_list = [i for i in range(1, int(n)+1)]
    zipped = zip(height_list, weight_list, idx_list)
    sorted_list = sorted(zipped, key=lambda x: (x[0], x[1], x[2]))
    result = ''
    for i in sorted_list:
        result += (str(i[2])+' ')
    print(result)


n = '5'
height = '120 90 110 90 180'
weight = '70 45 60 45 20'
sort_weightheight(n, height, weight)
