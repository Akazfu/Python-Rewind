while 1:
    def lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y
        while 1:
            if((greater % x == 0) and (greater % y == 0)):
                l = greater
                break
            greater += 1
        return l
    str_list = input().split()
    a, b = int(str_list[0]), int(str_list[1])
    print(lcm(a, b))
