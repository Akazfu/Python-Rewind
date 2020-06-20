# -*- coding:utf-8 -*-
# 求区间A和区间B的交集，需保证A[0]<B[0]
def intersection(A, B):
    # 不相交
    if A[1] < B[0]:
        return None
    if A[1] >= B[0]:
        return [B[0], A[1]]


# 合并区间列表
# 我们先将第一个区间放入result中，然后对于后面输入的区间的item[0]和result[-1][1]比，
# 如果result[-1][1] < item[0]，我们就将item加入到result，
# 否则话说明要放入的区间和result[-1]有重叠，那么我们取result[-1][1] = max(result[-1][1], item[1])
def merge(intervals):
    result = list()
    for item in intervals:
        if not result or result[-1][1] < item[0]:
            result.append(item)
        else:
            result[-1][1] = max(result[-1][1], item[1])

    return result


if __name__ == '__main__':
    in_ = [[0, 3], [1, 3], [3, 5], [3, 6]]

    # 长度，从0开始
    in_len = len(in_) - 1

    # 生成阶乘个数，如1234，则生成[1,2] [1,3] [1,4] [2,3] [2,4] [3,4]
    # indices = [[x, y] for x in range(0, in_len) for y in range(0, in_len + 1) if x < y]

    # 分别求这些下标对应的区间交集
    intersections = [intersection(in_[x], in_[y]) for x in range(0, in_len) for y in range(0, in_len + 1) if x < y]
    # 去除空集
    intersections = [z for z in intersections if z is not None]
    print(intersections)

    out_ = merge(intersections)
    print(out_)
