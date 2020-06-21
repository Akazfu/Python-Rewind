def intersection(A, B):
    if A[1] < B[0]:
        return None
    if A[1] >= B[0]:
        return [B[0], A[1]]


in_ = [[0, 3], [1, 3], [3, 5], [3, 6]]
in_len = len(in_) - 1

intersections = [intersection(in_[x], in_[y]) for x in range(
    0, in_len) for y in range(0, in_len + 1) if x < y]
intersections = [z for z in intersections if z is not None]

result = list()
for item in intersections:
    if not result or result[-1][1] < item[0]:
        result.append(item)
    else:
        result[-1][1] = max(result[-1][1], item[1])

new_list = []
for o in result:
    new_list.append(str(o[0]))
    new_list.append(str(o[1]))
print(' '.join(new_list))
