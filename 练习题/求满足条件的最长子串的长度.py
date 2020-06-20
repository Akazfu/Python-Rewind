# -*- coding:utf-8 -*-
def func(string):
    if len(string) < 2:
        return 0
    left = 0
    right = 1
    # 记录长度
    length = right - left + 1
    # 记录最大长度
    max_length = length
    # 记录上次右指针指向的是否为字母
    last = False

    while right != len(in_) and left <= right:
        if in_[left].isalpha() and in_[right].isalpha():
            left += 1
            right += 1
            last = True
        elif in_[left].isalpha() and in_[right].isdigit():
            length = right - left + 1
            max_length = max(length, max_length)
            right += 1
            last = False
        elif in_[left].isdigit() and in_[right].isdigit():
            length = right - left + 1
            max_length = max(length, max_length)
            right += 1
            last = False
        elif in_[left].isdigit() and in_[right].isalpha():
            if last:
                left = right
                right += 1
            else:
                left += 1
            last = True
    return max_length


if __name__ == '__main__':
    # 算法思想：
    # 使用滑动窗口，指定左右两个指针，当：
    # 1. 左指针指向字母，右指针指向字母：左右指针同时右移一位
    # 2. 左指针指向字母，右指针指向数字：左指针不动，右指针移一位
    # 3. 左指针指向数字，右指针指向数字：左指针不动，右指针移一位
    # 4. 左指针指向数字，右指针指向字母：
    #       4.1 当上次右指针也是字母时，左指针跳到右指针位置，右指针右移一位
    #       4.2 当上次右指针不是字母时，左指针右移一位，右指针不动
    # 当需要左指针不动，右指针移位的时候应该记录此时的字串长度

    # in_ = "abC124ACb"
    in_ = "da12bc3456e"
    in_ = "a5"

    print(func(in_))
