import random

l = random.sample(range(50), 10)
print(l)

length = len(l)
print(length)

empty = []
first = l[0]
last = l[9]

def firstlast():
    empty.append(first)
    empty.append(last)

firstlast()

print(empty)