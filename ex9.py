from random import *

n = randint(1, 9)
print(n) ##this is just for testing - comment out for real game.

g = int(input("Guess a number between 1 and 9: "))

while n!=g:
    if g<n:
        print("Too low")
        g = int(input("Try again: "))
    elif g>n:
        print("Too high")
        g = int(input("Try again: "))

if n==g:
    print("Correct!")
