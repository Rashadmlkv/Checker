#!/usr/bin/python3

import draw, ai
import pygame, sys, time

# 0 - white square, 1 - black square
# 3 - black , 5 - king
# 2 - white , 4 - king

pygame.init()
clock = pygame.time.Clock()
running = True
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
a, b, c, d = 0, 0, 0, 0  #ab piece located, cd moving square
turn = 0
rect = 100

def play_sound():
    pygame.mixer.music.load("assets/soundeffect.mp3")
    pygame.mixer.music.play()
def winlose():
    whitepiece = 0
    blackpiece = 0
    for i in range(len(board)):
        for k in range(len(board)):
            if board[i][k] == 3:
                blackpiece += 1
            elif board[i][k] == 2:
                whitepiece += 1

    if whitepiece == 0:
        print("Black win")
    elif blackpiece == 0:
        print("White win")

def get_pos(target):
    return target[1] // rect, target[0] // rect

#create board
board = [
         [0, 3, 0, 3, 0, 3, 0, 3],
         [3, 0, 3, 0, 3, 0, 3, 0],
         [0, 3, 0, 3, 0, 3, 0, 3],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]]



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #pygame.event.pump()
            running = 0 
        elif event.type == pygame.MOUSEBUTTONUP:
            a, b = get_pos(pygame.mouse.get_pos())
    
    winlose()
    
    if turn == 0:
        print("White's turn!")
    else:
        print("Black's turn!")

    draw.draw_board(board, screen)
    
    if turn == 0:
        ##a, b = [int(a) for a in input("Select piece: ").split()]        
        #is correct piece selected
        if (board[a][b] == 2):
            ##c, d = [int(a) for a in input("Select square: ").split()]
            if pygame.mouse.get_pressed() == (True, False, False):
                c, d = get_pos(pygame.mouse.get_pos())
            #move
            if (c == a - 1 and (d == b - 1 or d == b + 1) and board[c][d] == 1):
                board[a][b] = 1
                board[c][d] = 2
                play_sound()
            #attack
            elif ((c == a - 2 or c == a + 2) and board[c][d] == 1):
                #left attack
                if d == b - 2:
                    #forward
                    if c == a - 2 and (board[a-1][b-1] == 3 or board[a-1][b-1] == 5):
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a-1][b-1] = 1
                        play_sound()
                    #back
                    elif board[a+1][b-1] == 3 or board[a+1][b-1]==5:
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a+1][b-1] = 1
                        play_sound()
                    else:
                        print("can't attack")
                        continue

                #right attack
                if d == b + 2:
                    #forward
                    if c == a - 2 and board[a-1][b+1] == 3 or board[a-1][b+1] == 5:
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a-1][b+1] = 1
                        play_sound()
                    #back
                    elif board[a+1][b+1] == 3 or board[a+1][b+1] == 5:
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a+1][b+1] = 1
                        play_sound()
                    else:
                        print("can't attack")
                        continue

                #continue attack
                if (c < 6 and d > 1 and (board[c+1][d-1] == 3 or board[c+1][d-1] == 5) and board[c+2][d-2] == 1   #left bottom
                 or c < 6 and d < 6 and (board[c+1][d+1] == 3 or board[c+1][d+1] == 5) and board[c+2][d+2] == 1   #right bottom
                 or c > 1 and d > 1 and (board[c-1][d-1] == 3 or board[c-1][d-1] == 5) and board[c-2][d-2] == 1   #left upper
                 or c > 1 and d < 6 and (board[c-1][d+1] == 3 or board[c-1][d+1] == 5) and board[c-2][d+2] == 1): #right upper
                        for i in board:
                            print(i)
                        continue

            else:
                print("can't move")
                continue


            for i in board:
                print(i)

            turn = 1
        else:
            print("Select white piece")


    elif turn == 1:
        if ai.ai_make_move(board):
            turn = 0
        else:
            print("can't move")
    clock.tick(30)  # limits FPS to 30

