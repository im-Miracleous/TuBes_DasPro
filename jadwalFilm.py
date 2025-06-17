# File : jadwalFilm.py
# Penulis : Miracle Steven Gerrald
# Tujuan Program :
# Program menampilkan jadwal film yang tayang di bioskop Cinegaje

# Import Library
import csv
import os
import time

## Definisi Fungsi ##

# Fungsi deklarasiMatriks(d1, d2)
# Fungsi ini digunakan untuk mendeklarasikan matriks 2D dengan ukuran d1 x d2, dan akan mengembalikan nilai arr.
    # Kamus Lokal
    # arr : list 2D untuk menyimpan data film (list of lists)
    # d1 : jumlah baris matriks (int)
    # d2 : jumlah kolom matriks (int)
    # i : indeks untuk iterasi baris (int)
def deklarasiMatriks(d1, d2) :
    arr = [None] * d1
    for i in range(0, d1, 1):
        arr[i] = [None] * d2
    return arr

# Fungsi interface()
# Fungsi ini menampilkan interface menu utama untuk mengelola jadwal film.
    # Kamus Lokal
    # -
def interface():
    print("\n--------------------------------------------------")
    print("Pilihan Menu:")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Lihat Jadwal Film")
    print("4. Keluar")
    print("--------------------------------------------------\n")

# Fungsi jadwal_Film()
# Fungsi ini menampilkan jadwal film yang tersimpan dalam file 'films.csv'.
# Jika file tidak ada atau tidak ada data film yang tersimpan, akan menampilkan pesan yang sesuai.
    # Kamus Lokal
    # reader : objek pembaca CSV untuk membaca file 'films.csv'
    # f : objek file untuk membuka file 'films.csv'
    # os : modul untuk memeriksa keberadaan file
    # csv : modul untuk membaca dan menulis file CSV
    # rows : list untuk menyimpan baris-baris dari file CSV (list of lists)
    # header : list untuk menyimpan header dari file CSV (list)
    # film : list untuk menyimpan data film (list)
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

# Fungsi tambah_Film(N)
# Fungsi ini digunakan untuk menambahkan film baru ke dalam jadwal bioskop, di mana ia akan meminta input dari user untuk data film, menyimpan data tersebut ke dalam matriks, dan menyimpannya ke file 'films.csv'. Jika file 'films.csv' sudah ada, akan membaca jumlah film yang sudah ada untuk menentukan ID film berikutnya.
    # Kamus Lokal
    # N : jumlah film yang akan ditambahkan (int)
    # films : matriks 2D untuk menyimpan data film (list of lists)
    # file_exists : boolean untuk memeriksa apakah file 'films.csv' sudah ada (bool)
    # existing_rows : list untuk menyimpan baris-baris yang sudah ada dalam file 'films.csv' (list of lists)
    # next_id : ID film berikutnya yang akan digunakan (int)
    # id_num : ID film yang sedang diinput (int)
    # judul, jam, menit, genre, rating, tipe : variabel untuk menyimpan input dari user (str)
    # baris, kolom : jumlah baris dan kolom untuk tempat duduk berdasarkan tipe bioskop (int)
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

# Fungsi hapus_Film(N)
# Fungsi ini digunakan untuk menghapus film dari jadwal bioskop berdasarkan ID yang dimasukkan oleh user. Ia akan membaca file 'films.csv', menampilkan jadwal film, dan menghapus film yang dipilih. Setelah itu, ia akan memperbarui ID film dan menyimpan kembali ke file 'films.csv'.
    # Kamus Lokal
    # N : jumlah film yang akan dihapus (int)
    # reader : objek pembaca CSV untuk membaca file 'films.csv'
    # f : objek file untuk membuka file 'films.csv'
    # os : modul untuk memeriksa keberadaan file
    # deleted_ids : list untuk menyimpan ID film yang dihapus (list)
    # index : indeks film yang akan dihapus (int)
    # rows : list untuk menyimpan baris-baris dari file CSV (list of lists)
    # lines : list untuk menyimpan baris-baris dari file 'state_tempat_duduk.csv' (list of strings)
    # new_lines : list untuk menyimpan baris-baris baru setelah penghapusan (list of strings)
    # skip : boolean untuk menentukan apakah harus melewati baris tertentu (bool)
    # skip_count : jumlah baris yang harus dilewati (int)
    # idx : indeks untuk iterasi baris (int)
    # studio_counter : penghitung untuk ID studio yang tersisa (int)
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

# Fungsi harga_tiket(tipe)
# Fungsi ini mengembalikan harga tiket berdasarkan tipe bioskop yang dipilih.
    # Kamus Lokal
    # tipe : tipe bioskop yang dipilih (str)
    # price : harga tiket untuk tipe bioskop yang dipilih (int)
def harga_tiket(tipe):
    if (tipe == "Reguler/Deluxe"):
        price = 55000
    elif (tipe == "4DX"):
        price = 110000
    elif (tipe == "Premium Class"):
        price = 220000
    return price

# Fungsi tipe_bioskop()
# Fungsi ini menampilkan pilihan tipe bioskop dan meminta user untuk memilih salah satu, dan mengembalikan tipe yang dipilih.
    # Kamus Lokal
    # index_tipe : indeks tipe bioskop yang dipilih (int)
    # tipe : tipe bioskop yang dipilih (str)
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

# Fungsi simpan_state_tempat_duduk(studio_id, baris, kolom, filename='state_tempat_duduk.csv')
# Fungsi ini menyimpan state tempat duduk untuk studio tertentu ke dalam file 'state_tempat_duduk.csv'.
    # Kamus Lokal
    # studio_id : ID studio yang akan disimpan (int)
    # baris : jumlah baris tempat duduk (int)
    # kolom : jumlah kolom tempat duduk (int)
    # filename : nama file untuk menyimpan state tempat duduk (str)
def simpan_state_tempat_duduk(studio_id, baris, kolom, filename='state_tempat_duduk.csv'):
    import csv
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([])
        writer.writerow([studio_id])
        for _ in range(baris):
            writer.writerow(['V'] * kolom)


## PROGRAM UTAMA ##
    # Kamus Lokal
    # pilihan : pilihan menu yang dimasukkan oleh user (int)
    # N : jumlah film yang akan ditambahkan (int)
    # Ndel : jumlah film yang akan dihapus (int)
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