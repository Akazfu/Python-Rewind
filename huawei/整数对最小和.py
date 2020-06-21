array1 = '3 1 1 2'
array2 = '3 1 2 3'
k = '2'

list1 = [int(i) for i in array1.split()]
list2 = [int(i) for i in array2.split()]
len1 = list1.pop(0)
len2 = list2.pop(0)
combo_list = []

k = int(k)-1
quo, mod = divmod(k, len1)

for i in range(quo):
    for j in range(len1):
        combo_list.append(list2[i])
        combo_list.append(list1[j])
for i in range(mod+1):
    combo_list.append(list2[quo])
    combo_list.append(list1[i])
result = sum(combo_list)
print(result)
