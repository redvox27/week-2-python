#https://gist.github.com/guimaion/9275543
from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4
turn = 0
#xtra comment

#initializing board
board = []
rowList = []
columnList = []

for x in range(BOARD_SIZE):
 board.append(["O"] * BOARD_SIZE)


def print_board(board):
 for row in board:
     print (" ".join(row))

#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)

#define where the ship is
#ship_row = randint(0, BOARD_SIZE-1)
#ship_col = randint(0, BOARD_SIZE-1)

ship_row = 1
ship_col = 2

for turn in range(4) :
    guess_row = int(input("guess the row"))
    guess_column = int(input("guess the column"))

    if guess_row > 4:
        print("your row input is out of range")


    if guess_column > 4:
        print("your column input is out of range")

    if guess_row == ship_row:
        print("the row is guessed right")
        #rowList.append(guess_row)

    if guess_column == ship_col :
        print("the column is guessed right")
    #win if both the row and the column are guessed right
    if guess_row == ship_row and guess_column == ship_col :
        print("u won the game")
        break

    else:
        if guess_row in rowList :
            print("you already guessed this row")
        if guess_column in columnList :
            print("u already guessed this column")

        else:
            rowList.append(guess_row)
            columnList.append(guess_column)


    
if turn == NR_GUESSES-1:
 print ("Game Over")