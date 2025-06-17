# Import paket (packages)
import pygame
from pygame.locals import *
import sys
import pygwidgets

# Definisikan konstanta
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30
TIMER_LENGTH = 5

# Pengenalan dunia timer
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()

# Memanggil asset (gambar) yang dibutuhkan

# Pengenalan variabel
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Klik "Mulai" untuk menjalankan ' + str(TIMER_LENGTH) + ' detik: ', fontSize=36, justified='center', width=WINDOW_WIDTH)
startButton = pygwidgets.TextButton(window, (200, 100), 'Mulai')
clickMeButton = pygwidgets.TextButton(window, (320, 200), 'TEKAN DISINI')
timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Pesan ditampilkan ketika timer ditekan', fontSize=36, justified='center', width=WINDOW_WIDTH)
timerMessage.hide()
timerRunning = False
nFramesElapsed = 0
nFramesToWait = 0

# Perulangan
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            timerRunning = True
            nFramesElapsed = 0
            nFramesToWait = int(FRAMES_PER_SECOND * TIMER_LENGTH)
            startButton.disable()
            timerMessage.show()
            print('Perhitungan waktu dimulai')

        if clickMeButton.handleEvent(event):
            print('Tombol lain telah di klik')

    # Lakukan aksi per frame
    if timerRunning:
        nFramesElapsed += 1  # Increment frame elapsed
        if nFramesElapsed >= nFramesToWait:
            startButton.enable()
            timerMessage.hide()
            print('Waktu Habis')
            timerRunning = False

    # Bersihkan layar
    window.fill(WHITE)

    # Gambar semua elemen layar
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # Update layar
    pygame.display.update()

    # Buat perlahan
    CLOCK.tick(FRAMES_PER_SECOND)
