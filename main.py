#!/usr/bin/python3

import board as brd
import input as io
import draw as drw


running = True
turn = 3
board = brd.createBoard()
screen = drw.createWindow()

while running:
    #brd.printBoard(board)
    drw.drawBoard(board, screen)

    slcrow, slccol, isKing = io.getPiece(board, turn)
    drw.highliteSquare(screen, slcrow, slccol)
    dstrow, dstcol = io.getSquare(board, turn, slcrow, slccol, isKing)
    drw.drawAnim(screen, slcrow, slccol, dstrow, dstcol)
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

drw.quit()
