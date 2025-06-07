import csv
import datetime

def baca_data_seats(filename):
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]  # Menghapus baris kosong

    data = {}
    i = 0
    while i < len(rows):
        key = rows[i][0].strip().lower()
        i += 1
        if i < len(rows):
            value = rows[i][0].strip()
            data[key] = value
        i += 1

    # Parsing tambahan untuk tempat duduk dan state
    data['jumlah tiket'] = int(data.get('jumlah tiket', '0'))
    data['daftar tempat duduk'] = [x.strip() for x in data['daftar tempat duduk'].replace('"', '').split(',') if x.strip().lower() != "end"]

    # Membaca baris state tempat duduk yang tersisa
    state_rows = []
    while i < len(rows):
        row = [x.strip() for x in rows[i] if x.strip()]
        if row:
            state_rows.append(row)
        i += 1
    data['state tempat duduk'] = state_rows

    return data

# Contoh penggunaan
data = baca_data_seats("seats.csv")
tipe = data['tipe bioskop']
if tipe == "Reguler":
    harga = 55000
elif tipe == "4DX":
    harga = 110000
else:
    harga = 350000
    
# print(f"Jumlah Tiket:", data['jumlah tiket'])
# print(f"Daftar Tempat Duduk:", data['daftar tempat duduk'])


#   Resi -- Booking Tiket Bioskop --   #

def main():
    
    print(f"================================================")
    print(f"                Cinegaje Bioskop                ")
    print(f"------------------------------------------------")
    print(f" Detail Transaction     {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} ")
    print(f"                                                ")
    print(f" ------------------                             ")
    print(f" |                |  Fast X                     ")
    print(f" |                |                             ")
    print(f" |                |  Date: {datetime.datetime.now().strftime('%A, %d-%m-%Y')}  ")
    print(f" |                |  Time: {datetime.datetime.now().strftime('%H:%M')}         ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |  Booking Code: 9432940      ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" |                |                             ")
    print(f" ------------------                             ")
    print(f"                                                ")
    print(f" Transaction Ref : Cinegaje/RES/DD-YYYY/8349    ")
    print(f" Seats           :", data['daftar tempat duduk'] )
    print(f" Tipe Bioskop    :", tipe                        )
    print(f" Total tickets   :", data['jumlah tiket']        )
    print(f" Ticket Price    : Rp {harga}                   ")
    print(f" Promo/Diskon    : Rp 0                         ")
    print(f" Payment         : GOPAY/OVO/BCA/TUNAI/KREDIT   ")
    print(f"                                                ")
    print(f" Total Payment   :  Rp{data['jumlah tiket'] * harga}")
    print(f"                                                ")
    print(f"                                                ")
    print(f"              ==Selamat Menonton==              ")
    print(f"                    ==Enjoy==                   ")
    print(f"                                                ")
    print(f"================================================")
    
if __name__ == '__main__':    
    main()