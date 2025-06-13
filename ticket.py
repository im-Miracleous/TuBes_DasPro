import csv
import datetime

def baca_data_seats(filename="seats.csv"):
    """
    Fungsi ini membaca file seats.csv dan mengembalikan data dalam bentuk dictionary.
    """
    data = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row] # Membersihkan baris kosong

        i = 0
        while i < len(rows):
            key = rows[i][0].strip().lower()
            if key == 'judul film' and i + 1 < len(rows):
                data['judul_film'] = rows[i+1][0].strip()
                i += 2
            elif key == 'tipe bioskop' and i + 1 < len(rows):
                data['tipe_bioskop'] = rows[i+1][0].strip()
                i += 2
            elif key == 'jumlah tiket' and i + 1 < len(rows):
                data['jumlah_tiket'] = int(rows[i+1][0].strip())
                i += 2
            elif key == 'daftar tempat duduk' and i + 1 < len(rows):
                # Membersihkan string: hapus kutip, pisahkan dengan koma, dan hapus 'end'
                kursi_raw = rows[i+1][0].replace('"', '')
                data['daftar_kursi'] = [k.strip() for k in kursi_raw.split(',') if k.strip().lower() != 'end']
                i += 2
            elif key == 'state tempat duduk' and i + 1 < len(rows):
                state_raw = rows[i+1][0].replace('"', '')
                data['state_kursi'] = [s.strip() for s in state_raw.split(',') if s.strip().lower() != 'end']
                i += 2
            elif key == 'studio' and i + 1 < len(rows):
                data['studio'] = rows[i+1][0].strip()
                i += 2
            else:
                # Lewati baris yang tidak dikenali
                i += 1
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None

# --- BAGIAN LOGIKA UTAMA ---

def main():
    # 1. Baca data dari seats.csv
    data_tiket = baca_data_seats("seats.csv")

    if data_tiket:
        # Ambil data dari dictionary hasil pembacaan file
        judul_film = data_tiket.get('judul_film', 'N/A')
        tipe_bioskop_raw = data_tiket.get('tipe_bioskop', 'N/A')
        jumlah_tiket = data_tiket.get('jumlah_tiket', 0)
        daftar_tempat_duduk = data_tiket.get('daftar_kursi', ['-'])
        studio = data_tiket.get('studio', 'N/A')

        # Menggabungkan daftar kursi menjadi satu string
        kursi_str = ", ".join(daftar_tempat_duduk)
        tipe_bioskop_str = tipe_bioskop_raw

        # 3. Logika penentuan harga berdasarkan tipe bioskop
        harga_satuan = 0
        if 'reguler' in tipe_bioskop_str.lower() or 'deluxe' in tipe_bioskop_str.lower():
            harga_satuan = 60000
        elif '4dx' in tipe_bioskop_str.lower():
            harga_satuan = 110000
        elif 'premium' in tipe_bioskop_str.lower():
            harga_satuan = 350000
        
        total_harga = harga_satuan * jumlah_tiket
        # Format harga ke format mata uang Rupiah (contoh: Rp 240.000)
        harga_str = f"Rp {total_harga:,.0f}".replace(',', '.')

        # 4. Logika untuk Tanggal dan Waktu
        daftar_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        waktu_sekarang = datetime.datetime.now()
        nama_hari_ini = daftar_hari[waktu_sekarang.weekday()]
        tanggal_str = f"{nama_hari_ini}, {waktu_sekarang.strftime('%d-%m-%Y')}"
        waktu_str = waktu_sekarang.strftime('%H:%M')

        # --- BAGIAN TAMPILAN TIKET (OUTPUT) ---
        # F-string dengan alignment (<) untuk menjaga tata letak tetap rapi
        print(f"\033[1;36m" + "==============================================================")
        print(f"|             🎬 CINEMA Cinegaje - TIKET RESMI 🎬            |")
        print(f"|----------------------------------------------------------|   ")
        print(f"| 🎞️\t Film\t        {judul_film:<43}                           ") 
        print(f"| 📅\tDate\t       {tanggal_str:<43}                         ")
        print(f"| ⏰\tTime\t       {waktu_str:<43}                           ")
        print(f"| 🪑\tSeats\t       {kursi_str:<43}                          ")
        print(f"| 🎟️\t Tipe Bioskop\t{tipe_bioskop_raw:<43}                   ")
        print(f"| 🏢\tStudio\t       {studio:<43}                        ")
        print(f"| 💳\tHarga\t       {harga_str:<43}                          ")
        print(f"|----------------------------------------------------------|  ")
        print(f"|        📌 Tunjukkan tiket ini saat memasuki studio         |")
        print(f"==============================================================" + "\033[0m")

if __name__ == "__main__":
    main()