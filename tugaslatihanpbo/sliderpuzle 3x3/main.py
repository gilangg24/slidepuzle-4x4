# GAME SLIDER PUZLE

# 1 import modules
import pygame
from pygame.locals import *
import pygwidgets
import pyghelpers
import sys
from Game import *
from Constants import *

#2 define constans
WINDOW_WIDTH = 470
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30

#3 initialize
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#4 - load assets
import os
base_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(base_path, 'images')

restartButton = pygwidgets.CustomButton(window, (320, 455), 
                                       up=os.path.join(image_path, 'restartButtonUp.jpg'), 
                                       down=os.path.join(image_path, 'restartButtonDown.jpg'), 
                                       over=os.path.join(image_path, 'restartButtonover.jpg'))

#5 initial vatiable
clock = pygame.time.Clock()
timerDisplay = pygwidgets.DisplayText(window, (50, 465), '', fontSize=36, textColor=WARNA2)
messageDisplay = pygwidgets.DisplayText(window, (50, 510), 'Klik dijudul untuk dipindahkan', fontSize=24, textColor=WARNA2)

oGame = Game(window)
import os
base_path = os.path.abspath(os.path.dirname(__file__))
sounds_path = os.path.join(base_path, 'sounds')

soundBuzz = pygame.mixer.Sound(os.path.join(sounds_path, 'buzz.wav'))
soundApplause = oGame.soundApplause

oCountDownTimer = pyghelpers.CountDownTimer(TIMER_LENGHT)
oCountDownTimer.start()

#6 main loop
while True:
    print("Main loop iteration")
    #7 - event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Selamat, Anda menang')
                soundApplause.play()
                oCountDownTimer.stop()

        if restartButton.handleEvent(event):
            oGame.startNewGame()
            oCountDownTimer.start()

    # 8 - aksi per frame
    timeToShow = oCountDownTimer.getTimeInHHMMSS(2)
    timerDisplay.setValue('Waktu: ' + timeToShow)
    if oGame.getGamePlaying():
        if oCountDownTimer.ended():
            soundBuzz.play()
            messageDisplay.setText('Waktu habis')
            oGame.stopPlaying()

    # 9 - draw
    window.fill(WARNA1)

    try:
        oGame.draw()
    except Exception as e:
        print(f"Exception during oGame.draw(): {e}")
    restartButton.draw()

    timerDisplay.draw()
    messageDisplay.draw()

    # 10 update
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
