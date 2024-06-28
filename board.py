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
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [3, 0, 3, 0, 3, 0, 3, 0],
                [0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0]]
        return board

'''
    Reassign Board
    Become king
    in attack move check for double jump
'''
def updateBoard(board, turn, slcrow, slccol, dstrow, dstcol):
    contAttack = False

    if (dstrow == 0) or (dstrow == 7):
        board[dstrow][dstcol] = turn + 2
    else:
        board[dstrow][dstcol] = board[slcrow][slccol]

    board[slcrow][slccol] = 1

    if (slcrow - dstrow == 2) or (dstrow - slcrow == 2):
        board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] = 1
        contAttack = isContinue(board, turn, dstrow, dstcol)

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
        return running, "Black"
    elif (blacks == 0):
        print("WHITE WON!")
        running = False
        return running, "White"
    else:
        return True, None

'''
    Check for double jump
'''
def isContinue(board, turn, row, col):
    if turn == 3 or turn == 5:
        opp = 2
        next = [(-1, -1), (-1, +1)]
    else:
        opp = 3
        next = [(+1, -1), (+1, +1)]

    for (r, c) in next:
        if (1 <= (row + r) < 7) and (1 <= (col + c) < 7) and \
            board[row + r][col + c] == opp and \
            board[row + 2 * r][col + 2 * c] == 1:
            return True
        
    return False

def printBoard(board):
    for i in board:
        print(i)
