game = [
    [1, 1, 1],
	[2, 1, 0],
	[1, 1, 0]]

def win(egg):
    if egg[0][0] == egg[0][1] == egg[0][2] and egg[0][0] != 0:
        print("Winner - Player", egg[0][0])
    elif egg[1][0] == egg[1][1] == egg[1][2] and egg[1][0] != 0:
        print("Winner - Player", egg[1][0])
    elif egg[2][0] == egg[2][1] == egg[2][2] and egg[2][0] != 0:
        print("Winner - Player", egg[2][0])
    elif egg[0][0] == egg[1][0] == egg[2][0] and egg[0][0] != 0:
        print("Winner - Player", egg[0][0])
    elif egg[0][1] == egg[1][1] == egg[2][1] and egg[0][1] != 0:
        print("Winner - Player", egg[0][1])
    elif egg[0][2] == egg[1][2] == egg[2][2] and egg[0][2] != 0:
        print("Winner - Player", egg[0][2])
    elif egg[0][0] == egg[1][1] == egg[2][2] and egg[0][0] != 0:
        print("Winner - Player", egg[0][0])
    elif egg[0][2] == egg[1][1] == egg[2][0] and egg[0][2] != 0:
        print("Winner - Player", egg[0][2])
    else:
        print("No winner")

win(game)