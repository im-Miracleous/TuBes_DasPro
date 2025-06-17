# File : resi.py
# Penulis : Richard Vincentius Christian Dinata
# Tujuan Program :
# Program ini digunakan untuk membaca data kursi dari file CSV, menampilkan denah kursi, dan mencetak resi pembelian tiket bioskop.

import csv
import datetime

## Definisi Fungsi ##

# Fungsi baca_data_seats(filename)
# Fungsi ini membaca data kursi dari file CSV dan mengembalikan informasi terkait bioskop, jumlah tiket, daftar tempat duduk, dan status tempat duduk.
    # Kamus Lokal
    # tipe_bioskop : tipe bioskop yang dibaca dari file (str)
    # jumlah_tiket : jumlah tiket yang dibaca dari file (int)
    # daftar_tempat_duduk : daftar tempat duduk yang dibaca dari file (list of str)
    # studio : studio yang dibaca dari file (str)
    # state_tempat_duduk : status tempat duduk yang dibaca dari file (list of list of str)
    # i : indeks untuk iterasi melalui baris-baris file (int)
    # rows : daftar baris yang dibaca dari file CSV (list of list of str)
    # row : baris yang sedang diproses (list of str)
    # key : kunci untuk menentukan jenis data yang sedang dibaca (str)
    # x : variabel untuk iterasi dalam daftar tempat duduk (str)
def baca_data_seats(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]

    tipe_bioskop = None
    jumlah_tiket = None
    daftar_tempat_duduk = None
    studio = None
    state_tempat_duduk = []
    i = 0
    while i < len(rows):
        key = rows[i][0].strip().lower()
        if key == 'tipe bioskop' and i+1 < len(rows):
            tipe_bioskop = rows[i+1][0].strip().lower()
            i += 2
        elif key == 'jumlah tiket' and i+1 < len(rows):
            jumlah_tiket = int(rows[i+1][0].strip())
            i += 2
        elif key == 'daftar tempat duduk' and i+1 < len(rows):
            daftar_tempat_duduk = [x.strip() for x in rows[i+1][0].replace('"', '').split(',') if x.strip().lower() != "end"]
            i += 2
        elif key == 'studio' and i+1 < len(rows):
            studio = rows[i+1][0].strip().lower()
            i += 2
        else:
            row = [x.strip() for x in rows[i] if x.strip()]
            if row:
                state_tempat_duduk.append(row)
            i += 1
    return [tipe_bioskop, jumlah_tiket, daftar_tempat_duduk, state_tempat_duduk, studio]

# Fungsi tampilkan_denah_kursi(state_tempat_duduk, daftar_tempat_duduk)
# Fungsi ini menampilkan denah kursi bioskop berdasarkan status tempat duduk dan daftar tempat duduk yang sudah dipesan.
    # Kamus Lokal
    # rows : jumlah baris pada denah kursi (int)
    # cols : jumlah kolom pada denah kursi (int)
    # row_label : membuat label huruf (A, B, C, dst.) untuk setiap baris kursi bioskop (str)
    # seat_code : kode kursi yang sedang ditampilkan (str)
    # i, j : indeks untuk iterasi melalui baris-baris denah kursi (int)
def tampilkan_denah_kursi(state_tempat_duduk, daftar_tempat_duduk):
    print("\nDenah Kursi:")
    rows = len(state_tempat_duduk)
    cols = len(state_tempat_duduk[0]) if rows > 0 else 0
    for i in range(rows):
        row_label = chr(65 + i)
        print(f"{row_label}: ", end="")
        for j in range(cols):
            seat_code = f"{row_label}{j+1}"
            if seat_code in daftar_tempat_duduk:
                print("[ X ]", end=" ")
            else:
                print(f"[ {state_tempat_duduk[i][j]} ]", end=" ")
        print()

## PROGRAM UTAMA ##
    # Kamus Lokal
    # data : data yang dibaca dari file CSV (list)
    # tipe_bioskop_raw : tipe bioskop yang dibaca dari data (str)
    # jumlah_tiket : jumlah tiket yang dibaca dari data (int)
    # daftar_tempat_duduk : daftar tempat duduk yang dibaca dari data (list of str)
    # state_tempat_duduk : status tempat duduk yang dibaca dari data (list of list of str)
    # studio : studio yang dibaca dari data (str)
    # tipe : tipe bioskop yang ditentukan berdasarkan tipe_bioskop_raw (str)
    # harga : harga tiket berdasarkan tipe bioskop (int)
    # nama_film : nama film yang ditentukan berdasarkan data (str)
    # hari_ini : hari ini dalam format string (str)
    # promo : jumlah promo yang diberikan berdasarkan hari (int)
    # total_payment : total pembayaran yang dihitung berdasarkan jumlah tiket, harga, dan promo (int)
    # metode_tersedia : daftar metode pembayaran yang tersedia (list of str)
    # metode_pembayaran : metode pembayaran yang dipilih oleh user (str)
def main():
    data = baca_data_seats("seats.csv")
    tipe_bioskop_raw = data[0]
    jumlah_tiket = data[1]
    daftar_tempat_duduk = data[2]
    state_tempat_duduk = data[3]
    studio = data[4]

    if 'reguler' in tipe_bioskop_raw or 'deluxe' in tipe_bioskop_raw:
        tipe = "Reguler/Deluxe"
        harga = 55000
    elif '4dx' in tipe_bioskop_raw:
        tipe = "4DX"
        harga = 110000
    else:
        tipe = "Premium"
        harga = 350000

    # Fungsi child untuk mendapatkan nama film dari file CSV
    # Fungsi ini membaca file CSV dan mengembalikan nama film yang pertama ditemukan.
        # Kamus Lokal
        # get_nama_film : fungsi untuk mendapatkan nama film dari file CSV (function)
        # f : file handler untuk membaca file CSV (file object)
        # reader : objek pembaca CSV untuk membaca baris-baris file (csv.reader)
        # rows : daftar baris yang dibaca dari file CSV (list of list of str)
        # film : baris yang sedang diproses untuk mendapatkan nama film (list of str)
    def get_nama_film():
        try:
            with open('seats.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                for film in rows[1:]:
                    # if len(film) >= 4 and tipe_bioskop_raw in film[3].lower(): #! << buat apa ini?
                    print(film[0])
                    return film[0]
        except Exception:
            pass
        return "-"
    
    nama_film = get_nama_film()

    # === Tambahan Logika Promo/Diskon ===
    hari_ini = datetime.datetime.now().strftime('%A')
    if hari_ini in ['Friday', 'Saturday', 'Sunday']: # Promo hanya berlaku pada hari Jumat, Sabtu, dan Minggu
        promo = 10000
    else:
        promo = 0

    total_payment = jumlah_tiket * harga - promo

    # === Tambahan: Pilihan Metode Pembayaran ===
    metode_tersedia = ['GOPAY', 'OVO', 'BCA', 'TUNAI', 'KREDIT']
    while True:
        print("\nMetode pembayaran tersedia:", "/".join(metode_tersedia))
        metode_pembayaran = input("Silakan pilih metode pembayaran: ").strip().upper()
        if metode_pembayaran in metode_tersedia:
            break
        else:
            print("Metode tidak valid. Silakan pilih kembali.")

    # === Cetak Resi ===
    print(f"================================================")
    print(f"                Cinegaje Bioskop                ")
    print(f"------------------------------------------------")
    print(f" Detail Transaction     {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ")
    print(f"                                                ")
    print(f" ------------------                             ")
    print(f" |                |  {nama_film}             ")
    print(f" |                |                             ")
    print(f" |                |  Date: {datetime.datetime.now().strftime('%A, %d-%m-%Y')}  ")
    print(f" |                |  Time: {datetime.datetime.now().strftime('%H:%M')}         ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" ------------------                             ")
    print(f"                                                ")
    print(f" Transaction Ref : Cinegaje/RES/{datetime.datetime.now().strftime('%d%m%Y')}/8349")
    print(f" Studio          : {studio}")
    print(f" Seat            :", ", ".join(daftar_tempat_duduk))
    print(f" Tipe Bioskop    : {tipe}"                       )
    print(f" Total tickets   : {jumlah_tiket}"               )
    print(f" Ticket Price    : Rp {harga}"                   )
    print(f" Promo/Diskon    : Rp {promo}"                   )
    print(f" Payment         : {metode_pembayaran}"          )
    print(f"                                                ")
    print(f" Total Payment   : Rp {total_payment}"           )
    print(f"                                                ")
    print(f"              ==Selamat Menonton==              ")
    print(f"               ==Enjoy the Film==               ")
    print(f"================================================")

if __name__ == '__main__':    
    main()
