height_xiaoming, n = 100, 10
height_friends = [96, 97, 98, 100, 95, 101, 102, 103, 104, 105]
height_friends.sort()
difference = []
result = []

for friend in height_friends:
    difference.append(abs(friend - height_xiaoming))

output_list = [y for x, y in sorted(
    zip(difference, height_friends), key=lambda x: x[0])]
output_list = [str(i) for i in output_list]
output = ' '.join(output_list)
print(output)
