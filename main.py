# File : main.py
# Penulis : Miracle Steven Gerrald
# Tujuan Program : 
# Program menampilkan interface utama untuk aplikasi booking tiket bioskop

# Import Library
import jadwalFilm
import tempatduduk
import resi
import ticket
import time

## Definisi Fungsi ##

# Fungsi menu()
# Fungsi ini menampilkan menu utama aplikasi booking tiket bioskop dan menangani pilihan yang dipilih oleh user.
    # Kamus Lokal
    # choose : variabel untuk menyimpan pilihan menu yang dipilih oleh user (int)
def menu():
    print("\nSelamat datang di bioskop Cinegaje!")
    print('"Walau nonton tak jelas, abis nonton pasti puas!"')
    
    choose = 0
    while (choose != 3):
        print("\n----------------------------------------------------------------")
        print("Silahkan ketikkan angka sesuai menu yang ingin dipilih:")
        print("1. Lihat Jadwal Film")
        print("2. Booking Tiket")
        print("3. Keluar")
        print("----------------------------------------------------------------\n")
        choose = int(input("Pilihan: "))
        print("\n----------------------------------------------------------------")
        if (choose < 1 or choose > 3):
            print("Maaf, pilihan tidak valid. Silakan coba lagi.\n")
            time.sleep(2)
        if (choose == 1):
            jadwalFilm.jadwal_Film()
        elif (choose == 2):
            tempatduduk.main()
            print("Memproses pesanan tiket Anda...\n")
            time.sleep(7)
            resi.main()
            ticket.main()
        elif (choose == 3):
            print("\nKeluar dari program...\n")
            time.sleep(2)
            print("----------------------------------------------------------------")
    return

# Fungsi main()
# Fungsi ini adalah fungsi utama yang memanggil fungsi menu() untuk menjalankan aplikasi.
    # Kamus Lokal
    # -
def main():
    menu()
    
    return 0

if __name__ == '__main__':    
    main()