#!/usr/bin/python3

import pygame


board = [
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]]

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
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
        for j in range(4):
            pygame.draw.rect(screen, color, (posx, posy, width, height))
            posx += 100
        posy += 50
        if (i % 2 != 0):
            posx = 0
        else: posx = 50
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
