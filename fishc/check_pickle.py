import pickle
import os

filea1 = open('a1.pickle', 'rb')
filea1_t = pickle.load(filea1)

for line in filea1_t:
    print(line)

filea1.close()