import draw as drw
import pygame
pygame.init()
'''
    Check input is between index
    is player piece
    is king
'''
def getPiece(board, turn):
    while True:
        slcrow, slccol, deslc = drw.convertInput()
        try:
            #slcrow, slccol = [int(a) for a in input("Select piece: ").split()]
            if (slcrow < 0 or slcrow > 7) or (slccol < 0 or slccol > 7):
                print("Select integers between 0 & 7 !")
                continue
            elif board[slcrow][slccol] == turn + 2:
                return slcrow, slccol, True
            elif (board[slcrow][slccol] != turn):
                print("Select correct piece!")
                continue
            else:
                return slcrow, slccol, False

        except (ValueError, TypeError):
            print("Select only two integers!")

'''
    Check input is between index
    diogonal move
    black and empty square
    No more than 2 squares away
    No jumping on empty or self piece
    and if pawn, don't move backwards
'''
def getSquare(board, turn, slcrow, slccol, isKing):
    while True:
        dstrow, dstcol, deslc = drw.convertInput()
        if deslc:
            return 0, 0, 1
        try:
            #dstrow, dstcol = [int(a) for a in input("Select square: ").split()]
            if (dstrow < 0 or dstrow > 7) or (dstrow < 0 or dstcol > 7):
                print("Select integers between 0 & 7 !")
                continue

            elif (abs(dstrow - slcrow) != abs(dstcol - slccol)):
                print("Select diogonal square!")
                continue

            elif (board[dstrow][dstcol] != 1):
                print("Select empty and black square!")
                continue

            elif (slcrow - dstrow > 2) or (dstrow - slcrow > 2) or (slccol - dstcol > 2) or (dstcol - slccol > 2):
                print("Select at most two squares away!")
                continue

            elif (board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == 1 or board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == turn) and ((slcrow - dstrow == 2) or (dstrow - slcrow == 2)):
                print("Select attacable square!")
                continue

            elif (board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == 1 or board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == turn) and ((slcrow - dstrow == 2) or (dstrow - slcrow == 2)):
                print("Select attacable square!")
                continue

            elif not isKing:
                if (slcrow - dstrow < 0) and turn == 3:
                    print("Select forward move!")
                    continue

                elif (dstrow - slcrow < 0) and turn == 2:
                    print("Select forward move!")
                    continue

            return dstrow, dstcol, 0

        except (ValueError, TypeError):
            print("Select only two integers!")
