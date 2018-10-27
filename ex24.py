columns = int(input("How many columns would you like?: "))
rows = int(input("How many rows would you like?: "))

def top(r, c):
    for i in range(0, c):
        print(" ---", end = "")
    print("\r")

def board(r, c):
    for i in range(0, r):
        for i in range(0, (c+1)):
            print("|", end = "   ")
        print("\r")
        for i in range(0, c):
           print(" ---", end = "")
        print("\r")

top(rows, columns)
board(rows, columns)
