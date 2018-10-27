from random import *

with open("SOWPODS.txt", "r") as f:
    lines = f.readlines()

x = randint(0, len(lines))
print(lines[x])
