from random import randint

print("Think of a number between 0 and 100 and the computer will guess it")

comp = randint(0, 100)
print(comp)

hint = input("Was our number too high, too low or correct?")

x = 101
y = 0

while hint != "correct":
    if hint == "low":
        y = comp
        higher = randint(y+1, x)
        print(higher)
        comp = higher
    if hint == "high":
        x = comp
        lower = randint(y+1, x)
        print(lower)
        comp = lower

    hint = input("Was our number too high, too low or correct?")
