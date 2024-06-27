'''
    0 - White square,   1 - Black square
    2 - White pawn,     4 - White King
    3 - Black pawn,     5 - Black King
'''
def createBoard(color="Black"):
    if color == "Black":
        board = [
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [1, 0, 3, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [3, 0, 3, 0, 3, 0, 3, 0],
                [0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0]]
        return board
    elif color == "White":
        board = [
                [0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0],
                [0, 3, 0, 3, 0, 3, 0, 3],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [2, 0, 2, 0, 2, 0, 2, 0],
                [0, 2, 0, 2, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 0]]
        return board
    else:
        print("Unknown input!")

'''
    Reassign Board
    Become king
    in attack move check for double jump
'''
def updateBoard(board, turn, slcrow, slccol, dstrow, dstcol):
    contAttack = False

    if (dstrow == 0):
        board[dstrow][dstcol] = turn + 2
    else:
        board[dstrow][dstcol] = board[slcrow][slccol]

    board[slcrow][slccol] = 1

    if (slcrow - dstrow == 2) or (dstrow - slcrow == 2):
        board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] = 1
        contAttack = isContinue(board, dstrow, dstcol)

    return board, contAttack

'''
    Check game is finished
'''
def isFinish(board, running):
    whites, blacks = 0, 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 2 or board[i][j] == 4:
                whites += 1
            elif board[i][j] == 3 or board[i][j] == 5:
                blacks += 1

    if (whites == 0):
        print("BLACK WON!")
        running = False
        return running
    elif (blacks == 0):
        print("WHITE WON!")
        running = False
        return running
    else:
        return True

'''
    Check for double jump
'''
def isContinue(board, c, d):
    if (c < 6 and d > 1 and (board[c+1][d-1] == 3 or board[c+1][d-1] == 5) and board[c+2][d-2] == 1   #left bottom
            or c < 6 and d < 6 and (board[c+1][d+1] == 3 or board[c+1][d+1] == 5) and board[c+2][d+2] == 1   #right bottom
            or c > 1 and d > 1 and (board[c-1][d-1] == 3 or board[c-1][d-1] == 5) and board[c-2][d-2] == 1   #left upper
            or c > 1 and d < 6 and (board[c-1][d+1] == 3 or board[c-1][d+1] == 5) and board[c-2][d+2] == 1): #right upper
        return True


def printBoard(board):
    for i in board:
        print(i)
