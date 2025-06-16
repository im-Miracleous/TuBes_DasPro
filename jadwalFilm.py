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
    print("\n--------------------------------------------------")
    print("Pilihan Menu:")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Lihat Jadwal Film")
    print("4. Keluar")
    print("--------------------------------------------------\n")

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
    global recent_id
    films = deklarasiMatriks(N, 8)
    # Cek apakah file sudah ada dan baca jumlah film yang sudah ada
    file_exists = os.path.exists('films.csv')
    existing_rows = []
    if file_exists:
        with open('films.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            # Data film mulai dari baris ke-3 (indeks 2)
            existing_rows = rows[2:]
    next_id = len(existing_rows) + 1
    # Input data film
    print("\nMasukkan data jadwal film:")
    for i in range(N):
        id_num = next_id + i
        judul = input(f"Judul Film ke-{i+1}: ")
        jam = str(input(f"Jam Tayang Film ke-{i+1}: "))
        menit = str(input(f"Menit Tayang Film ke-{i+1}: "))
        genre = str(input(f"Genre Film: "))
        rating = str(input(f"Rating Usia: "))
        tipe = tipe_bioskop()
        studio = int(input(f"Studio: "))
        films[i][0] = id_num
        films[i][1] = judul
        films[i][2] = jam
        films[i][3] = menit
        films[i][4] = genre
        films[i][5] = rating
        films[i][6] = tipe
        films[i][7] = f"Studio {studio}"
        
        if tipe == "Reguler/Deluxe":
            baris = 10
            kolom = 20
        elif (tipe == "4DX"):
            baris = 8
            kolom = 16
        elif (tipe == "Premium Class"):
            baris = 5
            kolom = 6
        # Simpan state tempat duduk
        simpan_state_tempat_duduk(id_num, baris, kolom)
    
    # Debug print matriks films
    print("\nData film yang akan disimpan:")
    for film in films:
        print(film)
    
    # Simpan ke CSV
    write_header = not file_exists or os.stat('films.csv').st_size == 0
    with open('films.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["List Jadwal Film"])
            writer.writerow(["ID", "Judul Film", "Jam", "Menit", "Genre", "Rating", "Tipe", "Studio"])
        writer.writerows(films)
    return films

def hapus_Film(N):
    if os.path.exists('films.csv'):
        with open('films.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            if len(rows) > 2:
                print("\nJadwal Bioskop:")
                jadwal_Film()
                deleted_ids = []
                for i in range(N):
                    index = int(input(f"Masukkan nomor film yang ingin dihapus (1-{len(rows)-2}): "))
                    if 1 <= index <= len(rows) - 2:
                        deleted_id = rows[index + 1][0]
                        deleted_ids.append(deleted_id)
                        del rows[index + 1]
                    else:
                        print("Nomor tidak valid.")
                # Renumber IDs in films.csv
                for idx, row in enumerate(rows[2:], start=1):
                    if len(row) == 8:
                        row[0] = str(idx)
                with open('films.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                # Update state_tempat_duduk.csv
                if os.path.exists('state_tempat_duduk.csv'):
                    with open('state_tempat_duduk.csv', 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    new_lines = []
                    skip = False
                    skip_count = 0
                    for line in lines:
                        if skip:
                            skip_count -= 1
                            if skip_count == 0:
                                skip = False
                            continue
                        if line.strip() in deleted_ids:
                            # Determine how many seat rows to skip (count until next digit or EOF)
                            skip = True
                            skip_count = 0
                            idx = lines.index(line) + 1
                            while idx < len(lines) and not lines[idx].strip().isdigit():
                                skip_count += 1
                                idx += 1
                            continue
                        new_lines.append(line)
                    # Renumber remaining studio IDs
                    studio_counter = 1
                    for i, line in enumerate(new_lines):
                        if line.strip().isdigit():
                            new_lines[i] = f'{studio_counter}\n'
                            studio_counter += 1
                    with open('state_tempat_duduk.csv', 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
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
    if index_tipe == 1:
        tipe = "Reguler/Deluxe"
    elif index_tipe == 2:
        tipe = "4DX"
    elif index_tipe == 3:
        tipe = "Premium Class"
    return tipe

def simpan_state_tempat_duduk(studio_id, baris, kolom, filename='state_tempat_duduk.csv'):
    import csv
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([])
        writer.writerow([studio_id])
        for _ in range(baris):
            writer.writerow(['V'] * kolom)

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