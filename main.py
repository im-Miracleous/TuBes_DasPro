# File : main.py 
# Program menampilkan interface utama untuk aplikasi booking tiket bioskop

def menu():
    print("Selamat datang di bioskop Cinegaje!")
    print('"Walau nonton tak jelas, abis nonton pasti puas!"')
    print("--------------------------------------")
    print("Silahkan ketikkan angka sesuai menu yang ingin dipilih:")
    print("1. Lihat Jadwal Film")
    print("2. Booking Tiket")
    print("3. Histori Pesanan")
    print("4. Keluar")
    print("--------------------------------------")
    choose = int(input("Pilihan: "))
    print()
    return choose

def main():
    menu()
    
    return 0

if __name__ == '__main__':    
    main()