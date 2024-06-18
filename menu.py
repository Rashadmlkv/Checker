#!/usr/bin/python3

import pygame


board = [
         [0, 3, 0, 3, 0, 3, 0, 3],
         [3, 0, 3, 0, 3, 0, 3, 0],
         [0, 3, 0, 3, 0, 3, 0, 3],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
posx = 0
posy = 0
width = 50
height = 50
color = (255,0,0)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                pygame.draw.rect(screen, (255,255,255), (posx, posy, width, height))
                posx += 50
            elif board[i][j] == 1:
                pygame.draw.rect(screen, (255,0,0), (posx, posy, width, height))
                posx += 50
            elif board[i][j] == 3:
                pygame.draw.rect(screen, (255,0,0), (posx, posy, width, height))
                pygame.draw.circle(screen, (0,0,0), (posx + 25, posy + 25), 13)
                posx += 50
            elif board[i][j] == 2:
                pygame.draw.rect(screen, (255,0,0), (posx, posy, width, height))
                pygame.draw.circle(screen, (255,255,255), (posx + 25, posy + 25), 13)
                posx += 50

        posy += 50
        posx = 0


    if pygame.mouse.get_pressed() == (True, False, False):
        mousepos = pygame.mouse.get_pos()


    # flip() the display to put your work on screen


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
