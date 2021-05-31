import numpy 
import random
from collections import Counter

def dice():
    return random.randint(1, 6)

ret = []
for i in range(100):
    ret.append(numpy.random.choice(numpy.arange(1, 7), p=[0.32,0.32,0.12,0.04,0.07,0.13]))

retDict = Counter(ret)

print(retDict)
