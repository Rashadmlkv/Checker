import pygame, sys
pygame.init()

screenObj = pygame.display.Info()
screen20percent = screenObj.current_h / 100 * 20
screenHeight = screenObj.current_h - screen20percent
screenWidth = screenObj.current_h
#rgb
white = (241, 219, 191) 
black = (105, 130, 105)
back = (182, 199, 170)
highlite = (255, 176, 0)

#positions
posx, posy = 0, 0

#rectangle
rect = screenHeight // 8

whitepiece = pygame.image.load("assets/whitepiece.png")
blackpiece = pygame.image.load("assets/blackpiece.png")
whiteKingpiece = pygame.image.load("assets/whiteKingpiece.png")
blackKingpiece = pygame.image.load("assets/blackKingpiece.png")
limelogo = pygame.image.load("assets/limelogo.png")

button_width = 200
button_height = 50
centerx = screenWidth // 2
centery = screenHeight // 2
button_pvp = pygame.Rect(centerx - button_width, centery - (button_height * 2) - 20, button_width, button_height)
button_pve = pygame.Rect(centerx - button_width, centery - button_height - 10, button_width, button_height)
button_exit = pygame.Rect(centerx - button_width, centery + 10, button_width, button_height)
button_color = (246, 230, 203)
button_hover_color = (22, 48, 32)
font = pygame.font.Font(None, 36)

def createWindow():
    global screen
    screen = pygame.display.set_mode((screenHeight,screenHeight))
    pygame.display.set_icon(limelogo)
    pygame.display.set_caption('Lime Checkers')
    return screen

def draw_text(text, rect, screen):
    text_surface = font.render(text, True, (22, 48, 32))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)



def drawBoard(board , screen):
    screen.fill(back)
    global posx, posy
    print(rect)
    for i in range(8):
        for j in range(8):
            match board[i][j]:
                case 0:
                    pygame.draw.rect(screen, white, (posx, posy, rect, rect))
                    posx += rect

                case 1:
                    pygame.draw.rect(screen, black, (posx, posy, rect, rect))
                    posx += rect

                case 2:
                    pygame.draw.rect(screen, black, (posx, posy, rect, rect))
                    screen.blit(whitepiece, (posx, posy))
                    posx += rect

                case 3:
                    pygame.draw.rect(screen, black, (posx, posy, rect, rect))
                    screen.blit(blackpiece, (posx, posy))
                    posx += rect

                case 4:
                    pygame.draw.rect(screen, black, (posx, posy, rect, rect))
                    screen.blit(whiteKingpiece, (posx, posy))
                    posx += rect

                case 5:
                    pygame.draw.rect(screen, black, (posx, posy, rect, rect))
                    screen.blit(blackKingpiece, (posx, posy))
                    posx += rect

        posy += rect
        posx = 0

    posx=0
    posy=0
    pygame.display.flip()

def drawMenu(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if button_pvp.collidepoint(pos):
                    return
                if button_pve.collidepoint(pos):
                    return  
                if button_exit.collidepoint(pos):
                    pygame.quit()
                    sys.exit()

        screen.fill(back)
        screen.blit(pygame.transform.rotate(limelogo, 5), (screenWidth // 3, screenHeight // 1.7))
        screen.blit(limelogo, (screenWidth // 24, screenHeight // 6))
        screen.blit(limelogo, (screenWidth // 2, screenHeight // 9))

        # Draw buttons
        pygame.draw.rect(screen, button_color, button_pvp)
        pygame.draw.rect(screen, button_color, button_pve)
        pygame.draw.rect(screen, button_color, button_exit)

        # Draw button text
        draw_text("PvP", button_pvp, screen)
        draw_text("PvE", button_pve, screen)
        draw_text("Exit", button_exit, screen)

        pygame.display.flip()

def convertInput():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.event.pump()
                target = pygame.mouse.get_pos()
                return int(target[1] // rect), int(target[0] // rect), 0
        if pygame.mouse.get_pressed() == (0,0,1):
            return 0, 0, 1

def highliteSquare(screen, slcrow, slccol):
    pygame.draw.rect(screen, highlite, (slccol * rect, slcrow * rect, rect,rect), width = 5)
    pygame.display.flip()

def drawFinish(screen, winner):
    if winner is not None:
        rect2 = pygame.draw.rect(screen, button_color, button_start)
        draw_text(f"{winner} WON",rect2 ,screen)
        pygame.display.flip()
        pygame.time.wait(5000)
    
def playSound():
    pygame.mixer.music.load("assets/soundeffect.mp3")
    pygame.mixer.music.play()

def quit():
    pygame.quit()
