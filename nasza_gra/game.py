import pygame
import pygame.sysfont
from pygame.locals import *
from enum import Enum
import os
from PIL import Image
from random import randint

pygame.init()
pygame.mixer.init()
FPS = 15

# szerokość i wysokość okna gry
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# robienie sciezek wzglednych i czasami ladowanie
grafiki = os.path.dirname(__file__)
muzyka = os.path.dirname(__file__)
tekst = os.path.dirname(__file__)
MAINTHEME = os.path.join(muzyka, 'muzyka\intro.mp3')
Fight = os.path.join(muzyka, 'muzyka\Guardian Song.mp3')
BMUSIC = os.path.join(muzyka, 'muzyka\\background.mp3')
FMUSIC = os.path.join(muzyka, 'muzyka\\Guardian Song.mp3')
FIGHT_MUSIC = os.path.join(muzyka, 'muzyka\\Dragon_Castle.mp3')
ENEMY_SOUND = pygame.mixer.Sound('muzyka\\orc_sound.mp3')
FIGHT_SOUND = pygame.mixer.Sound('muzyka\\cios.wav')
ENEMY_ICON_1 = os.path.join(grafiki, 'grafiki\orc.png')
ENEMY_ICON_2 = os.path.join(grafiki, 'grafiki\slime1.png')
PBUTTON_L = os.path.join(grafiki, 'grafiki\start_L.png')
PBUTTON_D = os.path.join(grafiki, 'grafiki\start_D.png')
QBUTTON_L = os.path.join(grafiki, 'grafiki\quit_L.png')
QBUTTON_D = os.path.join(grafiki, 'grafiki\quit_D.png')
FBUTTON_L = os.path.join(grafiki, 'grafiki\\fight_L.png')
FBUTTON_D = os.path.join(grafiki, 'grafiki\\fight_D.png')
EBUTTON_L = os.path.join(grafiki, 'grafiki\\empty_L.png')
EBUTTON_D = os.path.join(grafiki, 'grafiki\\empty_D.png')
NBUTTON_L = os.path.join(grafiki, 'grafiki\\next_L.png')
NBUTTON_D = os.path.join(grafiki, 'grafiki\\next_D.png')
TBUTTON_L = os.path.join(grafiki, 'grafiki\\talk_L.png')
TBUTTON_D = os.path.join(grafiki, 'grafiki\\talk_D.png')
MAPA_NORMALNA = os.path.join(grafiki, 'grafiki\mapka1.png')
MAPA_KRAWEDZIE = os.path.join(grafiki, 'grafiki\mapka1_krawedzie.png')
M_FONT = os.path.join(grafiki, 'grafiki\PixelEmulator-xq08.ttf')
BACKGROUND = pygame.image.load(os.path.join(grafiki, 'grafiki\\backgronud1200x800.png'))
RAMKA_DIALOGU =  pygame.image.load(os.path.join(grafiki, 'grafiki\\ramka.png'))

# OKNO GRY
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Nasza gra')  # nazwa okna
CLOCK = pygame.time.Clock()
icon = pygame.image.load(os.path.join(grafiki, 'grafiki\player\player3.png'))
pygame.display.set_icon(icon)

# KOLORY
BLACK = (0, 0, 0)
BRIGHT_BLACK = (138, 138, 138)
WHITE = (255, 255, 255)

# JAKIES ZMIENNE DO IFOW
FIGHT = False
NPC = False
FLAG_MOUSE = True

# TEKST
FABULA = os.path.join(tekst, 'tekst\\fabula.txt')
with open(FABULA, 'r', encoding="UTF-8") as file:
    a = file.read()
STORY_BEGINNING = [a, a, "hejj ma zostac tylko a"]

with open(os.path.join(tekst, 'tekst\\npc1_10.txt'), 'r', encoding="UTF-8") as file:
    a = file.read()
NPC_1_DIALOG = [a]

with open(os.path.join(tekst, 'tekst\\npc2_10.txt'), 'r', encoding="UTF-8") as file:
    a = file.read()
with open(os.path.join(tekst, 'tekst\\npc2_15.txt'), 'r', encoding="UTF-8") as file:
    b = file.read()
with open(os.path.join(tekst, 'tekst\\npc2_20.txt'), 'r', encoding="UTF-8") as file:
    c = file.read()
with open(os.path.join(tekst, 'tekst\\npc2_25.txt'), 'r', encoding="UTF-8") as file:
    d = file.read()
'''NPC_2_DIALOG = [    open(os.path.join(tekst, 'tekst\\npc2_10.txt'), 'r', encoding="UTF-8"),
                    open(os.path.join(tekst, 'tekst\\npc2_15.txt'), 'r', encoding="UTF-8"),
                    open(os.path.join(tekst, 'tekst\\npc2_20.txt'), 'r', encoding="UTF-8"),
                    open(os.path.join(tekst, 'tekst\\npc2_25.txt'), 'r', encoding="UTF-8")  ]
'''
NPC_2_DIALOG = [a, b, c, d]
# FUNCKJE
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text, x, y, rozmiar=115):  # wyświetlanie wiadomości w grze
    largeText = pygame.font.SysFont(text, rozmiar)
    TextSurf, TextRect = text_objects(text, largeText, BLACK)
    TextRect.center = ((x), (y))
    SCREEN.blit(TextSurf, TextRect)
    pygame.display.update()

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

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
                warunek = True
                while(warunek):
                    SCREEN.blit(BACKGROUND, [0, 0])
                    czcionka = pygame.font.SysFont('Arial', 50)
                    blit_text(SCREEN, STORY_BEGINNING[0], (0, 0), czcionka)
                    for event in pygame.event.get():
                        whether_exit(event)
                    SCREEN.blit(pygame.image.load(PBUTTON_D), (450, 650))
                    MOUSE = pygame.mouse.get_pos()
                    CLICK = pygame.mouse.get_pressed()
                    if 455 < MOUSE[0] < 705 and 650 < MOUSE[1] < 750:
                        SCREEN.blit(pygame.image.load(PBUTTON_L), (450, 650))
                        if CLICK[0] == 1:
                            warunek = False
                    pygame.display.update()

                game_loop()
            elif action == 'quit':
                pygame.quit()
                quit()
            elif action == 'fight':
                global FIGHT
                FIGHT = True
            elif action == 'dialog':
                global NPC
                NPC = True
            elif action == 'next':
                global NPC_NUM, FLAG_MOUSE
                if FLAG_MOUSE:
                    NPC_NUM[3] += 1
                    FLAG_MOUSE = False
    else:
        SCREEN.blit(pygame.image.load(icolor), [x, y])


def m_menu():
    M_MENU = True
    music_play(MAINTHEME, -1)
    while M_MENU:

        for event in pygame.event.get():
            whether_exit(event)

        SCREEN.blit(BACKGROUND, [0, 0])  # kolor okna gry
        largeText = pygame.font.Font(M_FONT, 80)
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
mapa = pygame.image.load(MAPA_NORMALNA)
mapaX = -350
mapaY = -300
krawedzieX = -350
krawedzieY = -300
mapaX_step = 0
mapaY_step = 0


def mapa_wyswietl():
    global mapaX, mapaY
    SCREEN.blit(mapa, (mapaX, mapaY))


# PRZECIWNICY
# 0=x, 1=y, 2=hp, 3=ikonka
ENEMY_POSITIONS = [     [900, 700, 100, pygame.image.load(ENEMY_ICON_1)], [1700, 300, 100, pygame.image.load(ENEMY_ICON_1)],
                        [1800, 300, 50, pygame.image.load(ENEMY_ICON_2)], [1900, 300, 50, pygame.image.load(ENEMY_ICON_2)]] 
ENEMY_NUM = 0


def enemy():
    for enemy in ENEMY_POSITIONS:
        if enemy[2] < 0:  # jesli hp mniejsze od 0
            continue
        else:
            enemy[0] += mapaX_step
            enemy[1] += mapaY_step
            SCREEN.blit(enemy[3], (enemy[0], enemy[1]))
            ENEMY_SOUND.set_volume(0.1)

            if enemy[0] + 150 >= playerX >= enemy[0] - 30 and enemy[1] + 150 >= playerY >= enemy[1] - 50:
                global ENEMY_NUM
                ENEMY_NUM = enemy
                button(450, 650, FBUTTON_D, FBUTTON_L, 'fight')
                if not pygame.mixer.get_busy():  # jak nie ma if not to odtwarza kilka dźwięków jednocześnie
                    pygame.mixer.Sound.play(ENEMY_SOUND)


def fight():
    global FIGHT, ENEMY_NUM, FLAG_MOUSE
    wiadomosc = "No dalej, uderz go!"
    while FIGHT:
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(player_icon, (100, 500))
        SCREEN.blit(ENEMY_NUM[3], (900, 400))
        SCREEN.blit(RAMKA_DIALOGU, (0, 0))
        message_display("Click on enemy!", 600, 50, 80)

        for event in pygame.event.get():
            whether_exit(event)
        MOUSE = pygame.mouse.get_pos()
        CLICK = pygame.mouse.get_pressed()
        if CLICK[0] == 1 and FLAG_MOUSE == True:
            CLICK = (1, 0, 0)
            FLAG_MOUSE = False

        elif CLICK[0] == 1 and FLAG_MOUSE == False:
            CLICK = (0, 0, 0)

        elif CLICK[0] == 0:
            FLAG_MOUSE = True

        message_display(wiadomosc, 600, 150, 40)
        if 900 < MOUSE[0] < 1050 and 400 < MOUSE[1] < 541:
            if CLICK[0] == 1:
                dmg = randint(6, 17)
                ENEMY_NUM[2] -= dmg
                wiadomosc = ("Zadałeś przeciwnikowi " + str(dmg) + " obrazen")
                if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.play(FIGHT_SOUND)
                if ENEMY_NUM[2] <= 0:  # jesli hp <= 0
                    FIGHT = False
                music_play(BMUSIC, -1)

 # 0 = x, 1 = y, 2 = ikonka, 3 = ktory dialog, 4 = lista tekstow
NPC_POSITIONS = [   [1000, 350, pygame.image.load(os.path.join(grafiki, 'grafiki\\npc1.png')), int(0), NPC_1_DIALOG],
                    [1600, 500, pygame.image.load(os.path.join(grafiki, 'grafiki\\npc2.png')), int(0), NPC_2_DIALOG]   ] 

NPC_NUM = 0


def npc():
    global NPC_NUM, NPC
    NPC = False
    for npc in NPC_POSITIONS:
        npc[0] += mapaX_step
        npc[1] += mapaY_step
        SCREEN.blit(npc[2], (npc[0], npc[1]))

        if npc[0] + 50 >= playerX >= npc[0] - 50 and npc[1] + 50 >= playerY >= npc[1] - 50:
            NPC_NUM = npc
            button(450, 650, TBUTTON_D, TBUTTON_L, 'dialog')


def dialog():
    global NPC, NPC_NUM, FLAG_MOUSE, NPC_1_DIALOG
    while NPC:
        SCREEN.blit(RAMKA_DIALOGU, (0, 0))
        czcionka = pygame.font.SysFont('Arial', 40)
        blit_text(SCREEN,  NPC_1_DIALOG[NPC_NUM[3]], (0, 50), czcionka)
        button(450, 650, NBUTTON_D, NBUTTON_L, 'next')
        
        CLICK = pygame.mouse.get_pressed()  # zeby przytrzymanie przycisku wszystkiego nie psulo
        if CLICK[0] == 1:
            FLAG_MOUSE = False
        if CLICK[0] == 0 and FLAG_MOUSE == False:
            FLAG_MOUSE = True

        for event in pygame.event.get():
            whether_exit(event)
        pygame.display.update()


# poruszanie "sie"
def ruch_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step, player_direction, player_frame, player_stand, whether_leave_frame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player_stand = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                mapaY_step = 10
                player_direction = directions.up
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                mapaY_step = -10
                player_direction = directions.down
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                mapaX_step = 10
                player_direction = directions.left
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                mapaX_step = -10
                player_direction = directions.right
        if event.type == pygame.KEYUP:
            player_stand = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                mapaX_step = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_DOWN or event.key == pygame.K_s:
                mapaY_step = 0

        keys = pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            player_stand = False
            player_direction = directions.up
            mapaY_step = 10
        if keys[K_DOWN] or keys[K_s]:
            player_stand = False
            player_direction = directions.down
            mapaY_step = -10
        if keys[K_LEFT] or keys[K_a]:
            player_stand = False
            player_direction = directions.left
            mapaX_step = 10
        if keys[K_RIGHT] or keys[K_d]:
            player_stand = False
            player_direction = directions.right
            mapaX_step = -10

        whether_exit(event)
    player_frame, whether_leave_frame = set_frame(player_frame, player_stand, whether_leave_frame)


granica = Image.open(MAPA_KRAWEDZIE)
kolor_granicy = granica.convert("RGB")


def granica_mapy():
    global mapaX, mapaY, mapaX_step, mapaY_step, krawedzieX, krawedzieY, WINDOW_WIDTH, WINDOW_HEIGHT, kolor_granicy

    rgb_pixel_value = kolor_granicy.getpixel(
        (-mapaX + WINDOW_WIDTH / 2 - mapaX_step + 16, -mapaY + WINDOW_HEIGHT / 2 - mapaY_step + 20))  # ma być (0, 0, 0)

    if rgb_pixel_value == (0, 0, 0):
        mapaX_step = 0
        mapaY_step = 0
    else:
        mapaX += mapaX_step
        mapaY += mapaY_step
        krawedzieX += mapaX_step
        krawedzieY += mapaY_step


# PĘTLA GŁówna PROGRAMU
def game_loop():
    music_stop()
    music_play(BMUSIC, -1)
    while True:
        global mapaX, mapaY, mapaX_step, mapaY_step, FIGHT, krawedzieX, krawedzieY, NPC
        CLOCK.tick(FPS)
        if not FIGHT:
            SCREEN.fill(WHITE)
            mapa_wyswietl()
            gracz_wyswietl()
            enemy()
            npc()
            ruch_mapy()
            granica_mapy()
            # WALKA

            if NPC:
                mapa_wyswietl()
                gracz_wyswietl()
                enemy()
                dialog()

        else:
            music_stop()
            fight()

        pygame.display.update()  # aktualizuje wszystkie parametry ekranu na bieżąco


m_menu()
game_loop()
