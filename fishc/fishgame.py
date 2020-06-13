'''
游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。

a.假设游戏场景为范围（x,y）为0<=x<=10，0<=y<=10
b.游戏生成1只乌龟和10条鱼
c.它们的移动方向均随机
d.乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
e.当移动到场景边缘，自动向反方向移动
f.乌龟初始化体力为100（上限）
g.乌龟每移动一次，体力消耗1
h.当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
i.鱼暂不计算体力
j.当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
'''


import random


TURTLE_NUM = 1
FISH_NUM = 10
DIRECTIONS = ['up', 'down', 'left', 'right']


class Animal:
    def __init__(self, x_range=9, y_range=9):
        self.position = [random.randint(
            0, x_range), random.randint(0, y_range)]

    def move(self, step=1):
        self.step = step
        self.direction = random.choice(DIRECTIONS)

        if self.direction == 'up':
            if (self.position[1] + self.step) <= y_range:
                self.position[1] += self.step
            else:
                self.position[1] -= self.step
        elif self.direction == 'down':
            if (self.position[1] - self.step) >= 0:
                self.position[1] -= self.step
            else:
                self.position[1] += self.step
        elif self.direction == 'left':
            if (self.position[0] - self.step) >= 0:
                self.position[0] -= self.step
            else:
                self.position[0] += self.step
        elif self.direction == 'right':
            if (self.position[0] + self.step) <= x_range:
                self.position[0] += self.step
            else:
                self.position[0] -= self.step

        return self.position


class Turtle(Animal):
    stamina = 100

    def move(self):
        self.stamina -= 1
        self.step = random.randint(1, 2)
        super().move(self.step)
        return self.position

    def eat(self):
        self.stamina += 20


class Fish(Animal):
    def move(self):
        super().move()
        return self.position


list_range = input('输入游戏场景范围(最小是4 4)：').split()
x_range, y_range = int(list_range[0])-1, int(list_range[1])-1
game_round = 0

turtle = Turtle(x_range, y_range)
fish_list = []
for i in range(FISH_NUM):
    new_fish = Fish(x_range, y_range)
    fish_list.append(new_fish)
num_fish = len(fish_list)

while turtle.stamina > 0:
    if num_fish == 0:
        print('\n\n$$$$$ 已经吃光所有鱼，游戏胜利！$$$$$')
        break

    game_round += 1
    turtle.move()
    for fish in fish_list:
        fish.move()
        if fish.position == turtle.position:
            turtle.eat()
            fish_list.remove(fish)
            num_fish = len(fish_list)

    print('\n\n游戏回合：', game_round)
    print('乌龟当前体力：', turtle.stamina)
    print('乌龟选择的步数：', turtle.step)
    print('乌龟当前位置：', turtle.position)
    print('鱼当前的总数：', num_fish)
    print('鱼当前位置：', end=' ')
    for fish in fish_list:
        print(fish.position, end=' ')
else:
    print('\n\n***** 体力为零了，游戏失败！*****')
