a = input("Player 1 - Type: R/P/S: ")
b = input("Player 2 - Type: R/P/S: ")
a=a.upper()
b=b.upper()
if a == b:
    print("Draw!")

if a=="R" and b=="P":
    print("Player 2 wins!")

if a=="R" and b=="S":
    print("Player 1 wins!")

if a=="P" and b=="R":
    print("Player 2 wins!")

if a=="P" and b=="S":
    print("Player 1 wins!")

if a=="S" and b=="P":
    print("Player 2 wins!")

if a=="S" and b=="R":
    print("Player 1 wins!")

