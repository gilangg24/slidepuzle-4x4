# Card.py
import pygame
from Constants import * 

class Card():
    # Menginisialisasi font sekali untuk semua objek Card
    font = pygame.font.SysFont('Arial', 60, bold=True)

    def __init__(self, window, value, x, y):
        """
        Konstruktor untuk kelas Card.
        window: Objek jendela Pygame tempat kartu akan digambar.
        value: Nilai yang tersembunyi di balik kartu (misalnya, 'A', 'B', 1, 2).
        x, y: Koordinat kiri atas kartu.
        """
        self.window = window
        self.value = value
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT) # Area kartu untuk deteksi klik
        self.is_face_up = False # Status kartu: menghadap ke atas atau ke bawah
        self.is_matched = False # Status kartu: sudah cocok dan permanen terbuka

    def draw(self):
        """
        Menggambar kartu ke jendela Pygame berdasarkan statusnya (tertutup, terbuka, cocok).
        """
        if self.is_matched:
            # Jika kartu sudah cocok, gambar dengan warna cocok dan nilai terlihat
            pygame.draw.rect(self.window, MATCHED_CARD_COLOR, self.rect, border_radius=10)
            self._draw_value()
        elif self.is_face_up:
            # Jika kartu terbuka (tapi belum tentu cocok), gambar dengan warna muka dan nilai terlihat
            pygame.draw.rect(self.window, CARD_FACE_COLOR, self.rect, border_radius=10)
            self._draw_value()
        else:
            # Jika kartu tertutup, gambar dengan warna belakang
            pygame.draw.rect(self.window, CARD_BACK_COLOR, self.rect, border_radius=10)
            # Opsional: tambahkan logo atau pola di bagian belakang kartu
            pygame.draw.circle(self.window, TEXT_COLOR, self.rect.center, 20, 2) # Contoh: lingkaran di tengah

        # Menggambar batas di sekitar kartu
        pygame.draw.rect(self.window, TEXT_COLOR, self.rect, 2, border_radius=10)

    def _draw_value(self):
        """
        Metode bantu untuk menggambar nilai kartu di tengah.
        """
        # Render teks nilai kartu
        value_text = Card.font.render(str(self.value), True, BACKGROUND_COLOR)
        # Hitung posisi untuk menempatkan teks di tengah kartu
        text_rect = value_text.get_rect(center=self.rect.center)
        self.window.blit(value_text, text_rect)

    def flip(self):
        """
        Membalik status kartu (dari tertutup menjadi terbuka, atau sebaliknya).
        """
        if not self.is_matched: # Kartu yang sudah cocok tidak bisa dibalik lagi
            self.is_face_up = not self.is_face_up

    def get_value(self):
        """
        Mengembalikan nilai tersembunyi dari kartu ini.
        """
        return self.value

    def get_rect(self):
        """
        Mengembalikan objek Rect Pygame dari kartu ini untuk deteksi klik.
        """
        return self.rect

    def is_flipped(self):
        """
        Mengembalikan True jika kartu menghadap ke atas.
        """
        return self.is_face_up

    def is_card_matched(self):
        """
        Mengembalikan True jika kartu ini sudah cocok.
        """
        return self.is_matched

    def set_matched(self, matched=True):
        """
        Menetapkan status cocok untuk kartu ini.
        matched: Boolean, True untuk menandai cocok, False untuk tidak cocok.
        """
        self.is_matched = matched
        self.is_face_up = matched # Kartu yang cocok selalu menghadap ke atas

    def reset(self):
        """
        Mengatur ulang kartu ke status awal (tertutup dan tidak cocok).
        """
        self.is_face_up = False
        self.is_matched = False
