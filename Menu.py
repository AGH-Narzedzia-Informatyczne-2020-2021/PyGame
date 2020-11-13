import pygame
import pygame.sysfont
from pygame.locals import *

#pygame.sysfont.initsysfonts()
pygame.init()
FPS= 60

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 900

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra')
CLOCK = pygame.time.Clock()


#KOLORY
BACKGROUND_COLOR = (204, 255, 153)
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)



#FUNCKJE

def text_objects(text, font):
    textSurface= font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText= pygame.font.SysFont("Times New Roman", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    SCREEN.blit(TextSurf,TextRect)
    pygame.display.update()

#funkcja głównego menu
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
        largeText = pygame.font.SysFont('Arial', 115)
        TextSurf, TextRect = text_objects("Nasza Gra", largeText)  #zmienić nazwę jak już wymyślimy
        TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))
        SCREEN.blit(TextSurf, TextRect)

        # rysowanie obiektów
        MOUSE = pygame.mouse.get_pos()
        if 200 + 300 > MOUSE[0] > 200 and 600 + 120 > MOUSE[1] > 600:
            pygame.draw.rect(SCREEN, BRIGHT_BLACK, (200, 600, 300, 120))
        else:
            pygame.draw.rect(SCREEN, BLACK, (200, 600, 300, 120))
        if 700 + 300 > MOUSE[0] > 700 and 600 + 120 > MOUSE[1] > 600:
            pygame.draw.rect(SCREEN, BRIGHT_BLACK, (700, 600, 300, 120))
        else:
            pygame.draw.rect(SCREEN, BLACK, (700, 600, 300, 120))

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

        # zaktualizuj okno i wyświetl
        pygame.display.update()

m_menu()
game_loop()
# KONIEC