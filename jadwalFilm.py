# File : jadwalFilm.py 
# Program menampilkan jadwal film yang tayang di bioskop Cinegaje

# MASIH TENTATIVE!

import csv

def deklarasiMatriks(d1, d2) :
    arr = [None] * d1
    for i in range(0, d1, 1):
        arr[i] = [None] * d2
    return arr

def jadwal_Film():
    N = 5
    A = deklarasiMatriks(N, 3)  # Matriks untuk menyimpan jadwal film
    # Inisialisasi jadwal film
    for i in range(0, N, 1):
        A[i][0] = f"Film {i+1}"
    
    # Output
    print("Jadwal Bioskop:")
    print("--------------------------------------------------------------------")
    print("Judul Film\tJam Tayang\tHarga Tiket\tTipe Bioskop")
    print("--------------------------------------------------------------------")
    for i in range(0, N, 1):
        A[i][1] = f"{10 + i}:00"  # Jam tayang
        A[i][2] = f"Rp{50000 + (i * 10000)}"  # Harga tiket
        print(f"{A[i][0]}\t\t{A[i][1]}\t\t{A[i][2]}\t\tReguler")
    print("--------------------------------------------------------------------")
    print("Silahkan booking tiket sesuai jadwal film di atas!")

def main():
    jadwal_Film()
    return 0

if __name__ == '__main__':    
    main()