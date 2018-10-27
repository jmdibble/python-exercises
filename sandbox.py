game = [
    [0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

def oneGo():
    playerOne = input("Player 1, please type your move in co-ordinate form i.e. 'row,column': ")
    pOne = playerOne.split(",")
    pOnex = int(pOne[0])
    pOney = int(pOne[1])
    if game[pOnex - 1][pOney - 1] != "X" and game[pOnex - 1][pOney - 1] != "O":
        game[pOnex - 1][pOney - 1] = "X"
        print(game)
    else:
        print("Position already taken")
        return oneGo()


def twoGo():
    playerTwo = input("Player 2, please type your move in co-ordinate form i.e. 'row,column': ")
    pTwo = playerTwo.split(",")
    pTwox = int(pTwo[0])
    pTwoy = int(pTwo[1])
    if game[pTwox - 1][pTwoy - 1] != "X" and game[pTwox - 1][pTwoy - 1] != "O":
        game[pTwox - 1][pTwoy - 1] = "X"
        print(game)
    else:
        print("Position already taken")
        return twoGo()

for i in range(4):
    oneGo()
    twoGo()
oneGo()