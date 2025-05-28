# File : jadwalFilm.py 
# Program menampilkan jadwal film yang tayang di bioskop Cinegaje

# MASIH TENTATIVE!

import csv
import os

def deklarasiMatriks(d1, d2) :
    arr = [None] * d1
    for i in range(0, d1, 1):
        arr[i] = [None] * d2
    return arr

def jadwal_Film(N):
    if os.path.exists('films.csv'):
        with open('films.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 1:
                print("Jadwal Bioskop (dari CSV):")
                print("--------------------------------------------------------------------")
                print("\t".join(rows[0]))
                print("--------------------------------------------------------------------")
                for film in rows[1:]:
                    print("\t\t".join(film))
                print("--------------------------------------------------------------------")
                print("Silahkan booking tiket sesuai jadwal film di atas!")
            else:
                print("Belum ada data film yang tersimpan.")
    
    films = deklarasiMatriks(N, 5)
    print("Masukkan data jadwal film:")
    for i in range(N):
        judul = input(f"Judul Film ke-{i+1}: ")
        jam = int(input(f"Jam Tayang Film ke-{i+1}: "))
        menit = int(input(f"Menit Tayang Film ke-{i+1}: "))
        tipe = input(f"Tipe Bioskop Film ke-{i+1} (contoh Reguler): ")
        films[i][0] = judul
        films[i][1] = jam
        films[i][2] = menit
        films[i][4] = tipe
        
    # Simpan ke CSV
    with open('films.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Judul Film", "Jam", "Menit", "Harga Tiket", "Tipe Bioskop"])
        writer.writerows(films)
        
    return films


## PROGRAM UTAMA
def main():
    N = int(input("Masukkan jumlah film yang tayang: "))
    while N <= 0:
        print("Jumlah film harus lebih dari 0. Silakan coba lagi.")
        N = int(input("Masukkan jumlah film yang tayang: "))
    jadwal_Film(N)
    return 0

if __name__ == '__main__':    
    main()