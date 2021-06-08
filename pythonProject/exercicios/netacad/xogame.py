from random import randint


def line_style(n):
    if n == 1:
        print('+-------+-------+-------+')
    else:
        print('|       |       |       |')


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    for i in range(3):
        line_style(1)
        line_style(2)
        print(f'|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |')
        line_style(2)
    line_style(1)



def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    move = int(input('Enter your move: '))
    for i in range(3):
        if move in board[i]:
            ind = board[i].index(move)
            board[i][ind] = 'O'
            return victory_for(board, 'O')

    return print('Inválid number'), enter_move(board)


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    for i in range(3): # line
        sum = 0
        for j in range(3):
            if board[i][j] == sign:
                sum += 1
        if sum == 3:
            display_board(board)
            return print(f'{sign} WON')



    for i in range(3): # column
        sum = 0
        for j in range(3):
            if board[j][i] == sign:
                sum += 1
        if sum == 3:
            display_board(board)
            return print(f'{sign} WON')


    if sign == 'X':
        return enter_move(board)
    else: return draw_move(board)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    comp = randint(1, 9)
    for i in range(3):
        if comp in board[i]:
            ind = board[i].index(comp)
            board[i][ind] = 'X'
            display_board(board)
            return victory_for(board, 'X')
    return draw_move(board)



board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
display_board(board)
enter_move(board)