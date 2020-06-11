""" import math
import random
from pathlib import Path


class Dice:
    def __init__(self, dice1=None, dice2=None):
        self.dice1 = dice1
        self.dice2 = dice2

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        # outcome = (self.dice1, self.dice2)
        # return outcome
        return self.dice1, self.dice2

my_dice = Dice(6, 6)
print(my_dice.dice1, my_dice.dice2)
print(my_dice.roll())
print(type(my_dice.roll()))

path1 = Path("aa")
if path1.exists():
    path1.mkdir()
else:
    Path("cc").mkdir()
path = Path()
for file in path.glob('*.*'):
    print(file) """