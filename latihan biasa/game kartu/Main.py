# main.py
# GAME MEMORI

# 1. Mengimpor modul yang diperlukan
import pygame
from pygame.locals import *
import pygwidgets
import sys
import os
from Game import * 
from Constants import * 

# 2. Inisialisasi Pygame
pygame.init()
pygame.mixer.init() 

# Mengatur jendela permainan
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Memori")

# 3. Memuat aset (gambar tombol)
base_path = os.path.abspath(os.path.dirname(__file__))
image_path = os.path.join(base_path, 'images')

# Membuat tombol restart
try:
    restartButton = pygwidgets.CustomButton(window, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 60), 
                                           up=os.path.join(image_path, 'restartButtonUp.png'), 
                                           down=os.path.join(image_path, 'restartButtonDown.png'), 
                                           over=os.path.join(image_path, 'restartButtonOver.png'))
except FileNotFoundError:
    # Fallback jika gambar tidak ditemukan
    print("Peringatan: Gambar tombol restart tidak ditemukan. Menggunakan tombol teks.")
    restartButton = pygwidgets.TextButton(window, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 60), 
                                          'Mulai Ulang', fontSize=30, width=150, height=40,
                                          upColor=CARD_BACK_COLOR, downColor=CARD_FACE_COLOR,
                                          textColor=TEXT_COLOR)


# 4. Inisialisasi variabel dan objek game
clock = pygame.time.Clock() 
oGame = Game(window) 

# Menampilkan skor
scoreDisplay = pygwidgets.DisplayText(window, (50, SCREEN_HEIGHT - 80), 'Percobaan: 0', 
                                      fontSize=36, textColor=TEXT_COLOR)
# Menampilkan pesan game over/menang
messageDisplay = pygwidgets.DisplayText(window, (50, SCREEN_HEIGHT - 40), '', 
                                        fontSize=28, textColor=HIGHLIGHT_COLOR)

# 5. Loop utama permainan
while True:
    # 6. Penanganan peristiwa (event handling)
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN: 
            if not oGame.is_game_over(): 
                oGame.handle_click(event.pos)
            
        # Menangani peristiwa klik tombol restart
        if restartButton.handleEvent(event):
            oGame.start_new_game()
            messageDisplay.setText('') 

    # 7. Aksi per frame (logika permainan yang diperbarui setiap frame)
    oGame.update()

    # Perbarui tampilan skor
    scoreDisplay.setText(f'Percobaan: {oGame.get_score()}')

    # Periksa kondisi game over
    if oGame.is_game_over():
        messageDisplay.setText(f'Selamat! Anda menemukan semua pasangan dalam {oGame.get_score()} percobaan.')

    # 8. Menggambar elemen-elemen ke jendela
    window.fill(BACKGROUND_COLOR) # Mengisi seluruh jendela dengan warna latar belakang

    oGame.draw() # Menggambar semua kartu

    restartButton.draw() # Menggambar tombol restart
    scoreDisplay.draw() # Menggambar tampilan skor
    messageDisplay.draw() # Menggambar pesan

    # 9. Memperbarui tampilan dan mengontrol frame rate
    pygame.display.update()
    clock.tick(30) # Mengontrol frame rate menjadi 30 FPS
