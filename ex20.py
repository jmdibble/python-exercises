import random
a = random.sample(range(0, 9), 5)
b = random.randint(0, 9)

a.sort()
print(a)
print(b)

def match(x):
    if x in a:
        return True
    else:
        return False

if match(b) == True:
    print("Match")
else:
    print("No match")

