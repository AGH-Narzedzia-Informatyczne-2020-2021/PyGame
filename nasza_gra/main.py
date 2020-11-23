import pygame
import pygame.sysfont
from pygame.locals import *
import os
import time

# pygame.sysfont.initsysfonts()
pygame.init()
pygame.mixer.init()
FPS = 60

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych
grafiki = os.path.dirname(__file__)
muzyka = os.path.dirname(__file__)
MAINTHEME = os.path.join(muzyka, 'muzyka\intro.mp3')
BMUSIC = os.path.join(muzyka, 'muzyka\\background.mp3')
ENEMY_SOUND = os.path.join(muzyka, 'muzyka\\m_okay.mp3')
player_test_png = os.path.join(grafiki, 'grafiki\player_test.png')
ENEMY_ICON_png = os.path.join(grafiki, 'grafiki\orc.png')
map_dont_ask_png = os.path.join(grafiki, 'grafiki\map_dont_ask.png')
m_font = os.path.join(grafiki, 'grafiki\PixelEmulator-xq08.ttf')
BACKGROUND = pygame.image.load(os.path.join(grafiki, 'grafiki\\backgronud1200x800.png'))

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra')  # nazwa okna
CLOCK = pygame.time.Clock()
# icon = pygame.image.load('nazwa')  # zmiana ikonki
# pygame.display.set_icon(icon)

# KOLORY
# BACKGROUND = (204, 255, 153)
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)


# FUNCKJE

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):  # wyświetlanie wiadomości w grze
    largeText = pygame.font.SysFont(text, 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()


def whether_exit(event):  # tu nie ma petli for, tylko warunki
    if event.type == QUIT:
        pygame.quit()
        quit()
    elif event.type == pygame.KEYDOWN:
        if event.key == K_ESCAPE:  # wyjście escapem
            pygame.quit()
            quit()


def music_play(music, loops):
    pygame.mixer.music.load(music)  # intro
    pygame.mixer.music.set_volume(0.20)
    pygame.mixer.music.play(loops)


def music_stop():
    pygame.mixer.music.stop()


def button(msg, x, y, width, height, icolor, acolor,
           action=None):  # wymiary okna gry zostały zmienione zmienić lokalizaję przycisków

    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()
    if x + width > MOUSE[0] > x and y + height > MOUSE[1] > y:
        pygame.draw.rect(SCREEN, acolor, (x, y, width, height))
        if CLICK[0] == 1 and action != None:
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
    M_MENU = True
    music_play(MAINTHEME, -1)
    while M_MENU:

        for event in pygame.event.get():
            whether_exit(event)

        SCREEN.blit(BACKGROUND, [0, 0])  # kolor okna gry
        largeText = pygame.font.Font(m_font, 80)
        TextSurf, TextRect = text_objects("Medieval Adventure", largeText, BLACK)  # zmienić nazwę jak już wymyślimy
        TextRect.center = ((WINDOW_WIDTH / 2), (WINDOW_HEIGHT - 550))
        SCREEN.blit(TextSurf, TextRect)

        # rysowanie obiektów


        button('Zagraj', 200, 550, 300, 120, BLACK, BRIGHT_BLACK, 'play')
        button('Wyjdź', 700, 550, 300, 120, BLACK, BRIGHT_BLACK, 'quit')


# gracz
gracz_ikona = pygame.image.load(player_test_png)
playerX = WINDOW_WIDTH / 2
playerY = WINDOW_HEIGHT / 2


def gracz_wyswietl():
    global playerX, playerY
    SCREEN.blit(gracz_ikona, (playerX, playerY))


# mapa
mapa = pygame.image.load(map_dont_ask_png)
mapaX = 100
mapaY = 100
mapaX_step = 0
mapaY_step = 0

# przeciwnik
ENEMY_ICON = pygame.image.load(ENEMY_ICON_png)
ENEMYX = 1000
ENEMYY = 700


def enemy():
    global ENEMYX, ENEMYY
    ENEMYX += mapaX_step
    ENEMYY += mapaY_step
    SCREEN.blit(ENEMY_ICON, (ENEMYX, ENEMYY))
    #if (playerX <= ENEMYX-300 and playerY<= ENEMYY-300) or (playerX <= ENEMYX+300 and playerY <= ENEMYY+300):
        #pygame.mixer.Sound.play(pygame.mixer.Sound(ENEMY_SOUND))


def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mapaY_step = 10
            elif event.key == pygame.K_DOWN:
                mapaY_step = -10
            elif event.key == pygame.K_LEFT:
                mapaX_step = 10
            elif event.key == pygame.K_RIGHT:
                mapaX_step = -10

        # mapaX += mapaX_step
        # mapaY += mapaY_step

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_step = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mapaY_step = 0

        whether_exit(event)


# PĘTLA GŁówna PROGRAMU
def game_loop():
    music_stop()
    music_play(BMUSIC, -1)

    while True:
        global mapaX, mapaY, mapaX_step, mapaY_step

        CLOCK.tick(FPS)
        SCREEN.fill(WHITE)
        mapa_wyswietl()
        gracz_wyswietl()
        enemy()
        ruch_mapy()
        mapaX += mapaX_step
        mapaY += mapaY_step
        pygame.display.update()  # aktualizuje wszystkie parametry ekranu na bieżąco


m_menu()
game_loop()
