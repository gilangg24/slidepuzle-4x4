# File Utama Game Tebak Kartu

import pygame
from pygame.locals import *
import sys
import pygwidgets
import random
from Game import *

# definisikan nilai konstanta (ukuran layar untuk game)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# inisilisasi
pygame.init()
clock = pygame.time.clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'Game Baru', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (800, 530), 'Keluar', width=120, height=55)
                                   
oGame = oGame(window)

# looping foorever
while True:
    for event in pygame.event.get():
        if ((event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent():
            oGame.StartNewGame()