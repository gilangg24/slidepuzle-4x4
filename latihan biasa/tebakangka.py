import random

def tebak_angka():
    """
    Fungsi utama untuk menjalankan game Tebak Angka.
    """
    print("Selamat datang di game Tebak Angka!")
    print("Saya akan memikirkan sebuah angka antara 1 dan 100. Coba tebak!")

    # 1. Menentukan angka rahasia
    angka_rahasia = random.randint(1, 100)
    jumlah_percobaan = 0
    batas_percobaan = 7 # Pemain punya 7 kesempatan

    while jumlah_percobaan < batas_percobaan:
        try:
            # 2. Meminta input tebakan dari pemain
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_percobaan += 1

            # 3. Memeriksa tebakan pemain
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                # 4. Jika tebakan benar
                print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar dalam {jumlah_percobaan} percobaan.")
                break # Keluar dari loop karena sudah benar
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    else: # Ini akan dieksekusi jika loop while selesai tanpa break (batas percobaan tercapai)
        print(f"\nMaaf, Anda tolol dalam {batas_percobaan} percobaan. Angka rahasianya adalah {angka_rahasia}.")

# Memulai game
if __name__ == "__main__":
    tebak_angka()