#!/usr/bin/python3

import board as brd
import input as io
import draw as drw
import pygame


running = True
turn = 3
screen = drw.createWindow()

while running:
    drw.drawMenu(screen)
    game = True
    board = brd.createBoard()

    while game:
        drw.drawBoard(board, screen)
        slcrow, slccol, isKing = io.getPiece(board, turn)
        drw.highliteSquare(screen, slcrow, slccol)
        dstrow, dstcol, deslc = io.getSquare(board, turn, slcrow, slccol, isKing)

        if deslc:
            continue
    
        board, contAttack = brd.updateBoard(board, turn, slcrow, slccol, dstrow, dstcol)
        drw.playSound()
    
        if contAttack:
            continue
    
        game, winner = brd.isFinish(board, running)
        drw.drawFinish(screen, winner)

    

        print("========================")

        if (turn == 3) and game != False:
            turn = 2
            print("White's turn")

        elif game != False:
            turn = 3
            print("Black's turn")
drw.quit()
