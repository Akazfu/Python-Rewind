def move_tower(n, from_, mid_, to_):
    if n >= 1:
        move_tower(n-1, from_, to_, mid_)
        movedisk(n, from_, to_)
        move_tower(n-1, mid_,  from_, to_)


def movedisk(disk, from_, to_):
    print(f'移动盘子 {disk} 从 {from_} 到 {to_}。')


move_tower(32, 'x', 'y', 'z')
