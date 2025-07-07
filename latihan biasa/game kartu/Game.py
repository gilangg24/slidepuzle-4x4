# Game.py
import pygame
import random
from Card import *
from Constants import * 

class Game():
    def __init__(self, window):
        """
        Konstruktor untuk kelas Game.
        window: Objek jendela Pygame tempat game akan digambar.
        """
        self.window = window
        self.card_grid = []
        self.flipped_cards = [] 
        self.matches_found = 0 
        self.score = 0
        self.game_over = False 
        self.can_flip = True 
        self.flip_timer_start = 0 

        self.start_new_game() 

    def start_new_game(self):
        """
        Mengatur ulang dan menginisialisasi papan untuk permainan baru.
        """
        self.flipped_cards = []
        self.matches_found = 0
        self.score = 0
        self.game_over = False
        self.can_flip = True
        self.flip_timer_start = 0

        # Pastikan jumlah kartu genap untuk pasangan
        total_cards = GRID_COLS * GRID_ROWS
        if total_cards % 2 != 0:
            raise ValueError("Jumlah kartu harus genap untuk game memori.")
        
        num_pairs = total_cards // 2
        card_values_pool = [chr(65 + i) for i in range(num_pairs)]
        card_values = card_values_pool * 2 
        random.shuffle(card_values) 

        self.card_grid = []
        card_index = 0
        for row in range(GRID_ROWS):
            row_of_cards = []
            for col in range(GRID_COLS):
                # Menghitung posisi (x, y) untuk setiap kartu
                x = GRID_START_X + col * (CARD_WIDTH + MARGIN)
                y = GRID_START_Y + row * (CARD_HEIGHT + MARGIN)
                
                # Membuat objek Card dan menambahkannya ke grid
                card = Card(self.window, card_values[card_index], x, y)
                row_of_cards.append(card)
                card_index += 1
            self.card_grid.append(row_of_cards)

    def handle_click(self, mouse_pos):
        """
        Menangani klik mouse dari pemain.
        mouse_pos: Tuple (x, y) dari posisi klik mouse.
        """
        if self.game_over or not self.can_flip: 
            return

        for row in self.card_grid:
            for card in row:
                if card.get_rect().collidepoint(mouse_pos):
                    if not card.is_flipped() and not card.is_card_matched(): 
                        card.flip() # Balik kartu
                        self.flipped_cards.append(card) 

                        if len(self.flipped_cards) == 2: 
                            self.score += 1 
                            self.can_flip = False # 
                            self.flip_timer_start = pygame.time.get_ticks()

                        return # Keluar setelah menangani klik

    def update(self):
        """
        Memperbarui logika permainan setiap frame.
        Mengelola timer untuk membalik kartu kembali jika tidak cocok.
        """
        if self.game_over:
            return

        if not self.can_flip and pygame.time.get_ticks() - self.flip_timer_start > FLIP_DELAY_MS:
            # Delay telah berakhir, periksa apakah kartu cocok
            card1, card2 = self.flipped_cards[0], self.flipped_cards[1]

            if card1.get_value() == card2.get_value():
                # Kartu cocok! Tandai sebagai cocok
                card1.set_matched(True)
                card2.set_matched(True)
                self.matches_found += 1
            else:
                # Kartu tidak cocok, balik kembali
                card1.flip()
                card2.flip()
            
            self.flipped_cards = [] # Kosongkan daftar kartu yang terbuka
            self.can_flip = True # Aktifkan kembali kemampuan membalik kartu
            self.flip_timer_start = 0 # Reset timer

            # Periksa kondisi kemenangan
            if self.matches_found == (GRID_COLS * GRID_ROWS) // 2:
                self.game_over = True

    def draw(self):
        """
        Menggambar semua kartu di papan ke jendela Pygame.
        """
        for row in self.card_grid:
            for card in row:
                card.draw()

    def get_score(self):
        """
        Mengembalikan skor (jumlah percobaan).
        """
        return self.score

    def is_game_over(self):
        """
        Mengembalikan True jika permainan telah selesai.
        """
        return self.game_over
