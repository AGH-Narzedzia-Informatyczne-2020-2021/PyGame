import pygame
import pygame.sysfont
from pygame.locals import *

#pygame.sysfont.initsysfonts()
pygame.init()
FPS= 15

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra')
CLOCK = pygame.time.Clock()


# KOLORY
BACKGROUND_COLOR = (204, 255, 153)
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)

# FUNCKJE

def text_objects(text, font, color):
    textSurface= font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText= pygame.font.SysFont(text, 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    SCREEN.blit(TextSurf,TextRect)
    pygame.display.update()

def button(msg, x, y, width, height, icolor, acolor, action=None):
    MOUSE = pygame.mouse.get_pos()
    CLICK= pygame.mouse.get_pressed()
    if x + width > MOUSE[0] > x and y + height > MOUSE[1] > y:
        pygame.draw.rect(SCREEN, acolor, (x, y, width, height))
        if CLICK[0]== 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(SCREEN, icolor, (x, y, width, height))
    smallText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(msg, smallText, WHITE)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()

def m_menu():

    M_MENU= True

    while M_MENU:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
        SCREEN.fill(BACKGROUND_COLOR)  # kolor okna gry
        largeText = pygame.font.SysFont('Calibri', 115, bold=1 )
        TextSurf, TextRect = text_objects("Nasza Gra", largeText, BLACK)  #zmienić nazwę jak już wymyślimy
        TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT-600))
        SCREEN.blit(TextSurf, TextRect)

        # rysowanie obiektów
        MOUSE = pygame.mouse.get_pos()

        button('Zagraj', 200, 600, 300, 120, BLACK, BRIGHT_BLACK, 'play')
        button('Wyjdź', 700, 600, 300, 120, BLACK, BRIGHT_BLACK, 'quit')


        pygame.display.update()
        CLOCK.tick(FPS)


# PĘTLA GŁówna PROGRAMU


def game_loop():
    while True:
        CLOCK.tick(FPS)
        # obsługa zdarzeń generowanych przez gracza
        for event in pygame.event.get():
             if event.type == QUIT:
                pygame.quit()
                quit()
             elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
             print(event)
        #aktualizuje wszystkie parametry ekranu na bieżąco
        pygame.display.update()


m_menu()
game_loop()
# KONIEC