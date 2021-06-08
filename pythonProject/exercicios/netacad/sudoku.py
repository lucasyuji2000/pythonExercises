def create_board():
    board = []
    i = 1
    while i < 10:
        line = input(f'Enter {i}° line: ')
        if len(line) != 9:
            print('Invalid line')
            i -= 1
        else:
            board.append(line)
        i += 1
    return board


def line_validator(board):
    model = '123456789'
    for line in board:
        line = ''.join(sorted(line))
        if line != model:
            return False
    return True


def column_validator(board):
    model = '123456789'
    for i in range(9):
        column = ''
        for j in range(9):
            column += board[j][i]
        column = ''.join(sorted(column))
        if column != model:
            return False
    return True


def subsquares_validator(board):
    model = '123456789'
    for a in range(3):
        for b in range(3):
            subsquare = ''
            for c in range(3):
                for d in range(3):
                    subsquare += board[c+a*3][d+b*3]
                    subsquare = ''.join(sorted(subsquare))
            if subsquare != model:
                return False
    return True



# test = ['295743861', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '154938672']
# test1 = ['195743862', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '254938671']


board = create_board()


if line_validator(board) and column_validator(board) and subsquares_validator(board):
    print('YES')
else:
    print('NO')