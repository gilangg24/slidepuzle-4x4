# import paket (packages)pip
import pygame
from pygame.locals import *
import sys
import pygwidgets

# defiisikan konstanta
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30
TIMER_LENGHT = 2.5

# pengenalan dunia timer
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
# memanggil asset (gambar) yang dibutuhkan

# pengenalan variabel
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Klik "Mulai" untuk menjalankan' + str(TIMER_LENGHT) + ' detik: ', fontSize=36, justified= 'center', width=WINDOW_WIDTH)
startButton = pygwidgets.TextButton(window, (200, 100), 'Mulai')
clickMeButton = pygwidgets.TextButton(window, (320, 200), 'TEKAN DISINI')
timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Pesan ditampilkan ketika timer ditekan', fontSize=36, justified ='center', width=WINDOW_WIDTH)
timerMessage.hide()
timerRunning = False

# perulangan
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        if startButton.handleEvent(event):
            timerRunning = True
            nFramesElapsed = 0
            nFramesToWait = int (FRAMES_PER_SECOND * TIMER_LENGHT)
            startButton.disable()
            timerMessage.show()
            print ('Perhitungan waktu dimulai')
            timerRunning= True

        if clickMeButton.handleEvent(event):
            print('Tombol lain telah di klik')

# lakukan aksi perfper frame
    if timerRunning:
        nFramesElapsed = nFramesToWait + 1
        if nFramesElapsed >= nFramesToWait:
            startButton.enable()
            timerMessage.hide()
            print('Waktu Habis')
            timerRunning = False

    # Bersihkan layar
    window.fill(WHITE)

    # gambar semua element layar
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # update layar
    pygame.display.update()

    # dibuat perlahan
    CLOCK.tick(FRAMES_PER_SECOND)