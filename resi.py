import csv
import datetime
import jadwalFilm

def baca_data_seats(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]

    tipe_bioskop = None
    jumlah_tiket = None
    daftar_tempat_duduk = None
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
        else:
            row = [x.strip() for x in rows[i] if x.strip()]
            if row:
                state_tempat_duduk.append(row)
            i += 1
    return [tipe_bioskop, jumlah_tiket, daftar_tempat_duduk, state_tempat_duduk]

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

def main():
    data = baca_data_seats("seats.csv")
    tipe_bioskop_raw = data[0]
    jumlah_tiket = data[1]
    daftar_tempat_duduk = data[2]
    state_tempat_duduk = data[3]

    if 'reguler' in tipe_bioskop_raw or 'deluxe' in tipe_bioskop_raw:
        tipe = "Reguler/Deluxe"
        harga = 55000
    elif '4dx' in tipe_bioskop_raw:
        tipe = "4DX"
        harga = 110000
    else:
        tipe = "Premium"
        harga = 350000

    def get_nama_film():
        try:
            with open('films.csv', 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                for film in rows[2:]:
                    if len(film) >= 4 and tipe_bioskop_raw in film[3].lower():
                        return film[0]
        except Exception:
            pass
        return "-"
    nama_film = get_nama_film()

    # === Tambahan Logika Promo/Diskon ===
    hari_ini = datetime.datetime.now().strftime('%A')
    if hari_ini in ['Friday', 'Saturday', 'Sunday']:
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
    print(f" |                |  {nama_film:27}             ")
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
    print(f" Seats           :", ", ".join(daftar_tempat_duduk))
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
