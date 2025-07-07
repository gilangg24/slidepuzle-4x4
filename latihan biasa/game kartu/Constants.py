# Constants.py

# Ukuran Jendela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 720 # Diperbesar untuk UI

# Ukuran Kartu
CARD_WIDTH = 100
CARD_HEIGHT = 100

# Pengaturan Grid (harus menghasilkan jumlah kartu genap)
GRID_COLS = 4
GRID_ROWS = 4 # Total 16 kartu, 8 pasangan

# Margin (spasi) antar kartu dan dari tepi
MARGIN = 10

# Posisi Awal Grid (agar terpusat)
GRID_START_X = (SCREEN_WIDTH - (GRID_COLS * (CARD_WIDTH + MARGIN)) + MARGIN) // 2
GRID_START_Y = 50 # Jarak dari atas

# Warna (dalam format RGB)
BACKGROUND_COLOR = (20, 20, 20)      # Hitam gelap
CARD_BACK_COLOR = (50, 50, 150)      # Biru tua
CARD_FACE_COLOR = (200, 200, 255)    # Biru muda
MATCHED_CARD_COLOR = (50, 150, 50)   # Hijau untuk kartu yang cocok
TEXT_COLOR = (255, 255, 255)         # Putih
HIGHLIGHT_COLOR = (255, 255, 0)      # Kuning untuk highlight

# Pengaturan Game
FLIP_DELAY_MS = 1000 # Durasi (dalam milidetik) kartu tidak cocok tetap terbuka
