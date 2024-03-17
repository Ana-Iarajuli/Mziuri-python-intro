#TIC-TAC-TOE

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]
currentplayer = "X"
winner = None
gamerunning = True

def printBoard(board):
      print(board[0] + " | " + board[1] + " | " + board[2])
      print("----------")
      print(board[3] + " | " + board[4] + " | " + board[5])
      print("----------")
      print(board[6] + " | " + board[7] + " | " + board[8])

def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Sorry a player is already in that spot!!")
def horizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board[6]
        return True
def diag (board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def sworad(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkwin():
    if horizont(board) or diag(board) or sworad(board):
        print(f"the winner is {winner}")
def fre(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gamerunning = False

def playerswitch(board):
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

# def computer(board):
#     while currentplayer == "O":
#         position = random.randint(0, 8)
#         if board[position] == "-":
#             board[position] = "O"
#             playerswitch(board)

while gamerunning:
    printBoard(board)
    playerinput(board)
    checkwin()
    fre(board)
    playerswitch(board)
    # computer(board)
    # checkwin()
    # fre(board)
    # playerswitch(board)