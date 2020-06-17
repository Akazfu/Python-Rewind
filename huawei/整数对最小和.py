def intminsum(array1, array2, k):
    list1 = [int(i) for i in array1.split()]
    list2 = [int(i) for i in array2.split()]
    len1 = list1.pop(0)
    list2.pop(0)
    print(list1)
    print(list2)
    combo_list = []

    k = int(k)-1
    quo, mod = divmod(k, len1)

    for i in range(quo):
        for j in range(len1):
            combo_list.append(list1[j])
            combo_list.append(list2[i])

    for i in range(mod+1):
        combo_list.append(list1[i])
        combo_list.append(list2[quo])
    print(combo_list)
    result = sum(combo_list)
    print(len(combo_list))
    print(result)


array1 = '6 1 2 3 4 5 6'
array2 = '3 7 8 9'
k = '10'
intminsum(array1, array2, k)
