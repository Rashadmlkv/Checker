import pygame
pygame.init()
#rgb
white = (249, 249, 249)
red = (224, 20, 61)
black = (41, 39, 40)

#positions
posx, posy = 0, 0

#rectangle
rect = 100

def createWindow():
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((800, 800))

    return screen

def drawBoard(board , screen):
    global posx, posy
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                pygame.draw.rect(screen, white, (posx, posy, rect, rect))
                posx += rect
            elif board[i][j] == 1:
                pygame.draw.rect(screen, red, (posx, posy, rect, rect))
                posx += rect
            elif board[i][j] == 3:
                pygame.draw.rect(screen, red, (posx, posy, rect, rect))
                #pygame.draw.circle(screen, black, (posx + rect / 2, posy + rect/ 2), rect / 2.5)
                blackpiece = pygame.image.load("assets/blackpiece.png")
                screen.blit(blackpiece, (posx, posy))

                posx += rect
            elif board[i][j] == 2:
                pygame.draw.rect(screen, red, (posx, posy, rect, rect))
                #pygame.draw.circle(screen, white, (posx + rect / 2, posy+rect/2), rect / 2.5)
                whitepiece = pygame.image.load("assets/whitepiece.png")
                screen.blit(whitepiece, (posx, posy))
                posx += rect

        posy += rect
        posx = 0

    posx=0
    posy=0
    pygame.display.flip()

def convertInput():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                target = pygame.mouse.get_pos()
                return target[1] // rect, target[0] // rect

def highliteSquare(screen, slcrow, slccol):
    pygame.draw.rect(screen, "green", (slccol * rect, slcrow * rect, rect,rect), width = 5)
    pygame.display.flip()

def quit():
    pygame.quit()
