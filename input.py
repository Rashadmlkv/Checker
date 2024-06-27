def getPiece(board, turn):
    while True:
        try:
            slcrow, slccol = [int(a) for a in input("Select piece: ").split()]

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

def getSquare(board, turn, slcrow, slccol, isKing):
    while True:
        try:
            dstrow, dstcol = [int(a) for a in input("Select square: ").split()]
            
            if (dstrow < 0 or dstrow > 7) or (dstrow < 0 or dstcol > 7):
                print("Select integers between 0 & 7 !")
                continue
            elif (board[dstrow][dstcol] != 1):
                print("Select empty and black square!")
                continue

            if isKing:
                pieces = []
                row_step = 1 if dstrow > slcrow else -1
                col_step = 1 if dstcol > slccol else -1

                for i, j in zip(range(slcrow + row_step, dstrow, row_step), range(slccol + col_step, dstcol, col_step)):
                    pieces.append(board[i][j])

                enemy_pieces = [2, 4] if turn == 2 else [3, 5]
                own_pieces = [2, 4] if turn == 1 else [3, 5]

                if any(p in pieces for p in own_pieces):
                    print("Select an attackable square!")
                    continue

                if pieces.count(enemy_pieces[0]) > 1 or pieces.count(enemy_pieces[1]) > 1:
                    print("Select an attackable square!")
                    continue
            else:
                if (slcrow - dstrow > 2) or (dstrow - slcrow > 2) or (slccol - dstcol > 2) or (dstcol - slccol > 2):
                    print("Select at most two squares away!")
                    continue
                elif (board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == 1 or board[(dstrow + slcrow) // 2][(dstcol + slccol) // 2] == turn) and ((slcrow - dstrow == 2) or (dstrow - slcrow == 2)):
                    print("Select attacable square!3")
                    continue
            
            return dstrow, dstcol

        except (ValueError, TypeError):
            print("Select only two integers!")

def custom_range(start, end):
    if start < end:
        step = 1
    else:
        step = -1
    return range(start, end + step, step)
