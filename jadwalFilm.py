# File : jadwalFilm.py 
# Program menampilkan jadwal film yang tayang di bioskop Cinegaje

# MASIH TENTATIVE!

import csv
import os
import time

def deklarasiMatriks(d1, d2) :
    arr = [None] * d1
    for i in range(0, d1, 1):
        arr[i] = [None] * d2
    return arr

def interface():
    print("--------------------------------------------------")
    print("Pilihan Menu:")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Lihat Jadwal Film")
    print("4. Keluar")
    print("--------------------------------------------------")

def jadwal_Film():
    if os.path.exists('films.csv'):
        with open('films.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 2:
                print("\nJadwal Bioskop (dari database):")
                print("---------------------------------------------------------------------------------------------------------------------------")
                header = rows[1]
                print(f"{header[0]:5}{header[1]:20}{header[2]:>10}{header[3]:>10}{header[4]:>18}{header[5]:>20}{header[6]:>20}{header[7]:>20}")
                print("---------------------------------------------------------------------------------------------------------------------------")
                for film in rows[2:]:
                    if len(film) == 8:
                        print(f"{film[0]:5}{film[1]:20}{film[2]:>10}{film[3]:>10}{film[4]:>18}{film[5]:>20}{film[6]:>20}{film[7]:>20}")
                print("---------------------------------------------------------------------------------------------------------------------------")
            else:
                print("Belum ada data film yang tersimpan.")

def tambah_Film(N):
    films = deklarasiMatriks(N, 5)
    # Input data film
    print("\nMasukkan data jadwal film:")
    for i in range(N):
        judul = input(f"Judul Film ke-{i+1}: ")
        jam = str(input(f"Jam Tayang Film ke-{i+1}: "))
        menit = str(input(f"Menit Tayang Film ke-{i+1}: "))
        genre = str(input(f"Genre Film: "))
        rating = str(input(f"Rating Usia: "))
        films[i][0] = judul
        films[i][1] = jam
        films[i][2] = menit
        films[i][3] = genre
        films[i][4] = rating
    # Simpan ke CSV
    with open('films.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["List Jadwal Film"])
        writer.writerow(["Judul Film", "Jam", "Menit", "Genre", "Rating"])
        writer.writerows(films)
        writer.writerow([])  # Tambahkan baris kosong setelah data
    return films

def hapus_Film(N):
    if os.path.exists('films.csv'):
        with open('films.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 1:
                print("\nJadwal Bioskop:")
                print("-----------------------------------------------------------------------------------")
                header = rows[0]
                print(f"{header[0]:20}{header[1]:>10}{header[2]:>10}")
                print("-----------------------------------------------------------------------------------")
                for film in rows[1:]:
                    print(f"{film[0]:20}{film[1]:>10}{film[2]:>10}{film[3]:>18}{film[4]:>20}")
                print("-----------------------------------------------------------------------------------")
                # Hapus film
                for i in range(N):
                    index = int(input(f"Masukkan indeks film yang ingin dihapus (0-{len(rows)-2}): "))
                    if 0 <= index < len(rows) - 1:
                        del rows[index + 1]
                    else:
                        print("Indeks tidak valid.")
                # Simpan kembali ke CSV
                with open('films.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
            else:
                print("Belum ada data film yang tersimpan.")
    else:
        print("File films.csv tidak ditemukan.")

def harga_tiket(tipe):
    if (tipe == "Reguler/Deluxe"):
        price = 55000
    elif (tipe == "4DX"):
        price = 110000
    elif (tipe == "Premium Class"):
        price = 220000
    return price

def tipe_bioskop():
    index_tipe = 0
    while index_tipe < 1 or index_tipe > 3:
        print('\nTipe Bioskop:')
        print('1. Reguler/Deluxe\tRp55.000,00')
        print('2. 4DX\t\t\tRp110.000,00')
        print('3. Premium Class\tRp220.000,00')
        while (index_tipe < 1 or index_tipe > 3):
            index_tipe = int(input('\nPilih tipe bioskop (ketik angka 1-3): '))
            if (index_tipe < 1 or index_tipe > 3):
                print('Maaf tolong masukan angka di antara 1-3!')
    print('\n===============================================\n')
    if index_tipe == 1:
        tipe = "Reguler/Deluxe"
    elif index_tipe == 2:
        tipe = "4DX"
    elif index_tipe == 3:
        tipe = "Premium Class"
    return tipe

## PROGRAM UTAMA
def main():
    print("\nKONFIGURASI JADWAL FILM")
    print("Note: Selain staff, hanya admin yang dapat mengakses menu ini.")
    interface()
    pilihan = int(input("Masukkan pilihan menu (1-4): "))
    while (pilihan != 4):
        if (pilihan < 1 or pilihan > 4):
            print("Pilihan tidak valid. Silakan coba lagi.")
        if (pilihan == 1):
            N = int(input("Masukkan jumlah film yang tayang: "))
            while N <= 0:
                print("Jumlah film harus lebih dari 0. Silakan coba lagi.")
                N = int(input("Masukkan jumlah film yang tayang: "))
            tambah_Film(N)
        if (pilihan == 2):
            Ndel = int(input("Masukkan jumlah film yang ingin dihapus: "))
            while Ndel <= 0:
                print("Jumlah film harus lebih dari 0. Silakan coba lagi.")
                Ndel = int(input("Masukkan jumlah film yang ingin dihapus: "))
            hapus_Film(Ndel)
        if (pilihan == 3):
            jadwal_Film()
        interface()
        pilihan = int(input("Masukkan pilihan menu (1-4): "))
    print("Keluar dari program...")
    time.sleep(2)
    return 0

if __name__ == '__main__':    
    main()