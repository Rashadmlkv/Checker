#!/usr/bin/python3

import board as brd
import input as io

running = True
turn = 3
board = brd.createBoard()


while running:
    brd.printBoard(board)

    slcrow, slccol, isKing = io.getPiece(board, turn)
    dstrow, dstcol = io.getSquare(board, turn, slcrow, slccol, isKing)
    board, contAttack = brd.updateBoard(board, turn, slcrow, slccol, dstrow, dstcol)

    if contAttack:
        continue
    running = brd.isFinish(board, running)

    print("========================")

    if (turn == 3) and running != False:
        turn = 2
        print("White's turn")
    elif running != False:
        turn = 3
        print("Black's turn")

