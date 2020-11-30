import pygame
import pygame.sysfont
from pygame.locals import *
from enum import Enum
import os
from PIL import Image


pygame.init()
pygame.mixer.init()
FPS = 15

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych
grafiki = os.path.dirname(__file__)
muzyka = os.path.dirname(__file__)
MAINTHEME = os.path.join(muzyka, 'muzyka\intro.mp3')
BMUSIC = os.path.join(muzyka, 'muzyka\\background.mp3')
ENEMY_SOUND = pygame.mixer.Sound('muzyka\\m_okay.mp3')
ENEMY_ICON_png = os.path.join(grafiki, 'grafiki\orc.png')
PBUTTON_L = os.path.join(grafiki, 'grafiki\start_L.png')
PBUTTON_D = os.path.join(grafiki, 'grafiki\start_D.png')
QBUTTON_L = os.path.join(grafiki, 'grafiki\quit_L.png')
QBUTTON_D = os.path.join(grafiki, 'grafiki\quit_D.png')
mapa_normalna = os.path.join(grafiki, 'grafiki\mapka.png')
mapa_krawedzie = os.path.join(grafiki, 'grafiki\mapka_krawedzie.png')
m_font = os.path.join(grafiki, 'grafiki\PixelEmulator-xq08.ttf')
BACKGROUND = pygame.image.load(os.path.join(grafiki, 'grafiki\\backgronud1200x800.png'))


# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nasza gra')  # nazwa okna
CLOCK = pygame.time.Clock()
# icon = pygame.image.load('nazwa')  # zmiana ikonki
# pygame.display.set_icon(icon)

# KOLORY
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)


# FUNCKJE

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text):  # wyświetlanie wiadomości w grze
    largeText = pygame.font.SysFont(text, 115)
    TextSurf, TextRect = text_objects(text, largeText, BLACK)
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


def button(x, y, icolor, acolor, action=None):
    global FIGHT
    MOUSE = pygame.mouse.get_pos()
    CLICK = pygame.mouse.get_pressed()
    if x + 300 > MOUSE[0] > x and y + 120 > MOUSE[1] > y:
        SCREEN.blit(pygame.image.load(acolor), [x, y])
        if CLICK[0] == 1 and action != None:
            if action == 'play':
                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
            elif action == 'fight':
                global FIGHT
                FIGHT=True
    else:
        SCREEN.blit(pygame.image.load(icolor), [x, y])


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

        button(200, 525, PBUTTON_D, PBUTTON_L, 'play')
        button(700, 525, QBUTTON_D, QBUTTON_L, 'quit')
        pygame.display.update()


# kierunki
class directions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4


player_frames_stand = {directions.up: pygame.image.load(os.path.join(grafiki, 'grafiki\player\player0.png')),
                       directions.down: pygame.image.load(os.path.join(grafiki, 'grafiki\player\player3.png')),
                       directions.left: pygame.image.load(os.path.join(grafiki, 'grafiki\player\player6.png')),
                       directions.right: pygame.image.load(os.path.join(grafiki, 'grafiki\player\player9.png'))}

frames_up = [pygame.image.load(os.path.join(grafiki, 'grafiki\player\player1.png')),
             pygame.image.load(os.path.join(grafiki, 'grafiki\player\player2.png'))]
frames_down = [pygame.image.load(os.path.join(grafiki, 'grafiki\player\player4.png')),
               pygame.image.load(os.path.join(grafiki, 'grafiki\player\player5.png'))]
frames_left = [pygame.image.load(os.path.join(grafiki, 'grafiki\player\player7.png')),
               pygame.image.load(os.path.join(grafiki, 'grafiki\player\player8.png'))]
frames_right = [pygame.image.load(os.path.join(grafiki, 'grafiki\player\player10.png')),
                pygame.image.load(os.path.join(grafiki, 'grafiki\player\player11.png'))]

player_frames_move = {directions.up: frames_up, directions.down: frames_down, directions.left: frames_left,
                      directions.right: frames_right}
# gracz
player_icon = player_frames_stand[directions.down]
playerX = WINDOW_WIDTH / 2
playerY = WINDOW_HEIGHT / 2
player_frame = 0
player_direction = directions.down  # początkowy kierunek patrzenia
player_stand = True
whether_leave_frame = 0  # opóźnienie ruchu


# animacje gracza
def animations():
    global player_frame, player_direction, player_icon, player_frames_stand, player_frames_move, frames_up, frames_down, frames_left, frames_right
    if player_stand:
        player_icon = player_frames_stand[player_direction]
    elif whether_leave_frame == 0:
        player_icon = player_frames_move[player_direction][player_frame]
    return player_icon


def gracz_wyswietl():
    global playerX, playerY
    SCREEN.blit(animations(), (playerX, playerY))


def set_frame(player_frame, player_stand, whether_leave_frame):
    if player_stand == False:
        return (player_frame + 1) % 2, (whether_leave_frame + 1) % 3
    else:
        return player_frame, whether_leave_frame


# mapa
mapa = pygame.image.load(mapa_normalna)
mapaX = -150
mapaY = -300
krawedzieX = -150
krawedzieY = -300
mapaX_step = 0
mapaY_step = 0


def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# przeciwnik
ENEMY_ICON = pygame.image.load(ENEMY_ICON_png)


ENEMY_POSITIONS = [[1000, 700], [200, 200]]

def enemy():
    for enemy in ENEMY_POSITIONS:
        enemy[0]+=mapaX_step
        enemy[1] += mapaY_step
        SCREEN.blit(ENEMY_ICON, (enemy[0], enemy[1]))
        ENEMY_SOUND.set_volume(0.1)
        if enemy[0] + 250 >= playerX >= enemy[0] - 30 and enemy[1] + 300 >= playerY >= enemy[1] - 50:
            button(300, 700, QBUTTON_D, QBUTTON_L, 'fight')
            if not pygame.mixer.get_busy():  # jak nie ma if not to odtwarza kilka dźwięków jednocześnie
                pygame.mixer.Sound.play(ENEMY_SOUND)

time=0
def fight():
    #while True:
      #  global time
       # time+=1
       # print("COS",time)

        pygame.mixer.music.pause()
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(player_icon, (100, 500))
        SCREEN.blit(ENEMY_ICON, (1000, 600))


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step, player_direction, player_frame, player_stand, whether_leave_frame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player_stand = False
            if event.key == pygame.K_UP:
                mapaY_step = 10
                player_direction = directions.up
            if event.key == pygame.K_DOWN:
                mapaY_step = -10
                player_direction = directions.down
            if event.key == pygame.K_LEFT:
                mapaX_step = 10
                player_direction = directions.left
            if event.key == pygame.K_RIGHT:
                mapaX_step = -10
                player_direction = directions.right
        if event.type == pygame.KEYUP:
            player_stand = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mapaX_step = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                mapaY_step = 0

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            player_stand = False
            player_direction = directions.up
            mapaY_step = 10
        if keys[K_DOWN]:
            player_stand = False
            player_direction = directions.down
            mapaY_step = -10
        if keys[K_LEFT]:
            player_stand = False
            player_direction = directions.left
            mapaX_step = 10
        if keys[K_RIGHT]:
            player_stand = False
            player_direction = directions.right
            mapaX_step = -10

        whether_exit(event)
    player_frame, whether_leave_frame = set_frame(player_frame, player_stand, whether_leave_frame)



granica = Image.open(mapa_krawedzie)
kolor_granicy = granica.convert("RGB")

def granica_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step, krawedzieX, krawedzieY, WINDOW_WIDTH, WINDOW_HEIGHT, kolor_granicy
    rgb_pixel_value = kolor_granicy.getpixel( (-mapaX + WINDOW_WIDTH/2 - mapaX_step, -mapaY + WINDOW_HEIGHT/2 - mapaY_step) ) # ma być (0, 0, 0)
    print(rgb_pixel_value)
    if rgb_pixel_value == (0, 0, 0):
        mapaX_step = 0
        mapaY_step = 0
    else:
        mapaX += mapaX_step
        mapaY += mapaY_step
        krawedzieX += mapaX_step
        krawedzieY += mapaY_step


FIGHT = False

# PĘTLA GŁówna PROGRAMU
FIGHT = False

def game_loop():
    music_stop()
    music_play(BMUSIC, -1)
    while True:
        global mapaX, mapaY, mapaX_step, mapaY_step, FIGHT, krawedzieX, krawedzieY
        CLOCK.tick(FPS)
        if not FIGHT:
            SCREEN.fill(WHITE)
            mapa_wyswietl()
            gracz_wyswietl()
            enemy()
            ruch_mapy()
            granica_mapy()  
            # WALKA
        else:
            fight()

        pygame.display.update()  # aktualizuje wszystkie parametry ekranu na bieżąco


m_menu()
game_loop()

