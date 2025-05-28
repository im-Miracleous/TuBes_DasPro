# File : main.py 
# Program menampilkan interface utama untuk aplikasi booking tiket bioskop

import jadwalFilm
import tempatduduk
import resi

def menu():
    print("Selamat datang di bioskop Cinegaje!")
    print('"Walau nonton tak jelas, abis nonton pasti puas!"')
    print("--------------------------------------")
    print("Silahkan ketikkan angka sesuai menu yang ingin dipilih:")
    print("1. Lihat Jadwal Film")
    print("2. Booking Tiket")
    print("3. Print Resi")
    print("4. Keluar")
    print("--------------------------------------")
    choose = int(input("Pilihan: "))
    while (choose != 4):
        if (choose == 1):
            jadwalFilm.lihat_jadwal_film()
        elif (choose == 2):
            tempatduduk.main()
        elif (choose == 3):
            resi.main()
        elif (choose == 4):
            print("Keluar dari program...")
        choose = int(input("Pilihan: "))
    return

def main():
    menu()
    
    return 0

if __name__ == '__main__':    
    main()