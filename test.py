#!/usr/bin/python3

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers Game Menu')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.Font(None, 74)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        screen.fill(WHITE)
        
        draw_text('Checkers Game', font, BLACK, screen, 200, 100)
        
        mx, my = pygame.mouse.get_pos()
        
        button_start = pygame.Rect(200, 250, 400, 100)
        button_exit = pygame.Rect(200, 400, 400, 100)
        
        if button_start.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                start_game()
        if button_exit.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        
        pygame.draw.rect(screen, GREEN, button_start)
        pygame.draw.rect(screen, RED, button_exit)
        
        draw_text('Start', font, BLACK, screen, 350, 275)
        draw_text('Exit', font, BLACK, screen, 375, 425)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def start_game():
    print("Game Started!")
    # Implement your game loop here
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_text('Checkers Game Running', font, BLACK, screen, 100, 250)
        
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()

