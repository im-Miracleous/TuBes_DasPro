# File : jadwalFilm.py 
# Program menampilkan jadwal film yang tayang di bioskop Cinegaje

# MASIH TENTATIVE!

import csv

def lihat_jadwal_film():
    with open('films.csv', mode='r') as file:
        reader = csv.reader(file)
        print("Jadwal Film di Bioskop Cinegaje")
        print("--------------------------------------")
        print("No. | Judul Film | Jam Tayang | Durasi | Genre | Ruangan")
        print("--------------------------------------")
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]}")
        print("--------------------------------------")

def inputFilm():
    loop = True
    while (loop == True):
        with open('films.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            judul = input("Judul Film\b: ")
            jam_tayang = input("Jam Tayang\b: ")
            durasi = input("Durasi\b: ")
            genre = input("Genre\b: ")
            ruangan = input("Ruangan\b: ")
            writer.writerow([judul, jam_tayang, durasi, genre, ruangan])
            print("Film berhasil ditambahkan!")
        tanya = input("Apakah Anda ingin menambahkan film lain? (y/n): ")
        if tanya.lower() != 'y':
            loop = False
            print("Kembali ke menu utama...")
            print()

def main():
    lihat_jadwal_film()
    inputFilm()
    return 0

if __name__ == '__main__':    
    main()