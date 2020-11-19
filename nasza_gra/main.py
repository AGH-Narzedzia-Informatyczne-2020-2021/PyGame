import pygame
import pygame.sysfont
from pygame.locals import *
import os

#pygame.sysfont.initsysfonts()
pygame.init()
FPS= 15

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych
grafiki = os.path.dirname(__file__)
player_test_png = os.path.join(grafiki, 'grafiki\player_test.png')
map_dont_ask_png = os.path.join(grafiki, 'grafiki\map_dont_ask.png')

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra') # nazwa okna
#CLOCK = pygame.time.Clock()
#icon = pygame.image.load('nazwa')  # zmiana ikonki
#pygame.display.set_icon(icon)

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


def whether_exit():
    for event in pygame.event.get():    # wyjście
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:   # wyjście escapem
                pygame.quit()
                quit()


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
        whether_exit()
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
        #CLOCK.tick(FPS)

# gracz
gracz_ikona = pygame.image.load(player_test_png)
def gracz_wyswietl():
    SCREEN.blit(gracz_ikona, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

# mapa
mapa = pygame.image.load(map_dont_ask_png)
mapaX = -1000
mapaY = -2000
mapaX_krok = 0
mapaY_krok = 0

def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_krok, mapaY_krok
    for event in pygame.event.get():
        '''if event.type == pygame.KEYDOWN:
            print("key stroked")
            if event.key == pygame.K_UP:
                mapaY_krok = 100
                print("www")
            elif  event.key == pygame.K_DOWN:
                mapaY_krok = -100
                print("sss")
            elif  event.key == pygame.K_LEFT:
                mapaX_krok = 100
                print("aa")
            elif  event.key == pygame.K_RIGHT:
                mapaX_krok = -100
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mapaY_krok = 0
                print("wswsws w gore dol")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_krok = 0
                print("adadad w lewo prawo")'''
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mapaX_krok = 5
                print("klikam w lewo")
            if event.key == pygame.K_RIGHT:
                mapaX_krok = -5
                print("klikam w prawo")
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_krok = 0
                print("zwalniam przycisk")

# PĘTLA GŁówna PROGRAMU
def game_loop():
    running = True
    while running:
        #CLOCK.tick(60)
        #print("jakis tekst")
        global mapaX, mapaY, mapaX_krok, mapaY_krok
        whether_exit()
        SCREEN.fill( (255, 0, 0) )
        #ruch_mapy()

        #mapaX += mapaX_krok
        #mapaY += mapaY_krok
        mapa_wyswietl()
        gracz_wyswietl()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("klikam w lewo")
                if event.key == pygame.K_RIGHT:
                    print("klikam w prawo")
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    print("zwalniam przycisk")

        pygame.display.update()     #aktualizuje wszystkie parametry ekranu na bieżąco

m_menu()
# KONIEC