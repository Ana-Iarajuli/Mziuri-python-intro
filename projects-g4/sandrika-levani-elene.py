from random import randrange

def display_board(board):
    print("+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ", board[0][0],"  |  ", board[0][1], "  |  ", board[0][2], "  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n",
          "|       |       |       |\n",
          "|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |\n",
          "|       |       |       |\n",
          "+-------+-------+-------+\n", )

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter your move: "))
    if 1 <= move <= 9:
        row, column = (move - 1) // 3, (move - 1) % 3
        if board[row][column] == move:
            board[row][column] = 'O'
        else:
            print("Already occupied. Try again")
            enter_move(board)
    else:
        print("Unknown move. Try again")
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['O', 'X']:
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == sign:
        return True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == sign:
        return True
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == sign:
        return True
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == sign:
        return True
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == sign:
        return True
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == sign:
        return True
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == sign:
        return True
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == sign:
        return True
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    move = randrange(len(free_fields))
    row, column = free_fields[move]
    board[row][column] = 'X'

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board(board)
while True:
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print('You won!')
        break

    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print('Computer won!')
        break

    if not make_list_of_free_fields(board):
        print("It's a tie")
        break