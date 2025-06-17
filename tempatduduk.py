import csv
import jadwalFilm

def deklarasiMatriks(dimensi1,dimensi2) :
    arr = [None]*dimensi1 # array berisi 3 elemen
    for i in range(0,dimensi1,1):
        arr[i] = [None]*dimensi2
    return arr

def isiAlfabetMatriks(baris, kolom):
    matriks = deklarasiMatriks(baris, kolom)
    for i in range(0, baris, 1):
        for j in range(0, kolom, 1):
            if (i+1 == 1):
                matriks[i][j] = 'A'
            elif (i+1 == 2):
                matriks[i][j] = 'B'
            elif (i+1 == 3):
                matriks[i][j] = 'C'
            elif (i+1 == 4):
                matriks[i][j] = 'D'
            elif (i+1 == 5):
                matriks[i][j] = 'E'
            elif (i+1 == 6):
                matriks[i][j] = 'F'
            elif (i+1 == 7):
                matriks[i][j] = 'G'
            elif (i+1 == 8):
                matriks[i][j] = 'H'
            elif (i+1 == 9):
                matriks[i][j] = 'I'
            elif (i+1 == 10):
                matriks[i][j] = 'J'
            elif (i+1 == 11):
                matriks[i][j] = 'K'
            elif (i+1 == 12):
                matriks[i][j] = 'L'
            elif (i+1 == 13):
                matriks[i][j] = 'M'
            elif (i+1 == 14):
                matriks[i][j] = 'N'
            elif (i+1 == 15):
                matriks[i][j] = 'O'
            elif (i+1 == 16):
                matriks[i][j] = 'P'
            elif (i+1 == 17):
                matriks[i][j] = 'Q'
            elif (i+1 == 18):
                matriks[i][j] = 'R'
            elif (i+1 == 19):
                matriks[i][j] = 'S'
            elif (i+1 == 20):
                matriks[i][j] = 'T'
            elif (i+1 == 21):
                matriks[i][j] = 'U'
            elif (i+1 == 22):
                matriks[i][j] = 'V'
            elif (i+1 == 23):
                matriks[i][j] = 'W'
            elif (i+1 == 24):
                matriks[i][j] = 'X'
            elif (i+1 == 25):
                matriks[i][j] = 'Y'
            elif (i+1 == 26):
                matriks[i][j] = 'Z'
    return matriks

def ambil_tipe_dari_id(id_film):
    with open('films.csv', mode='r', encoding='utf-8') as file:
        next(file)  # Lewati baris "List Jadwal Film"
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['ID']) == id_film:
                return row['Tipe']        
    print("\n❌ ID film tidak ditemukan dalam state_tempat_duduk.csv")
    return None  # jika ID tidak ditemukan

def ambil_ukuran_dari_tipe(tipe):
    global baris, kolom
    if tipe == "Reguler/Deluxe":
        baris = 10  # max 26 huruf , 2D 10, 4DX 8
        kolom = 20  # max 2 digit , 2D 20, 4DX 16
    elif (tipe == "4DX"):
        baris = 8
        kolom = 16
    elif (tipe == "Premium Class"):
        baris = 5
        kolom = 6
    else:
        raise ValueError("Tipe bioskop tidak dikenal")

def ambil_state_kursi(id_film):
    global baris, kolom
    matrix = []
    selesai = False

    with open("state_tempat_duduk.csv", newline="", encoding="utf-8") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines) and not selesai:
        line = lines[i].strip()

        if line == str(id_film):
            i += 1
            while i < len(lines) and not selesai:
                line_kursi = lines[i].strip()
                if line_kursi.isdigit():  # ID film berikutnya
                    selesai = True
                elif line_kursi:  # baris kursi valid
                    matrix.append([kursi.strip() for kursi in line_kursi.split(',')])
                i += 1
        else:
            i += 1
    return matrix

def simpan_state_kursi(film_id, matrix):
    filename = 'state_tempat_duduk.csv'

    # Baca semua isi file
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Cari posisi ID film
    i = 0
    found = False
    result = []
    while i < len(lines):
        if lines[i].strip() == str(film_id):
            found = True
            # Gantikan baris-baris berikut dengan data baru
            result.append(f"{film_id}\n")
            for row in matrix:
                result.append(",".join(row) + "\n")
            i += len(matrix) + 1  # Lewati baris lama
        else:
            result.append(lines[i])
            i += 1

    # Kalau ID belum ditemukan, tambahkan di akhir
    if not found:
        result.append(f"{film_id}\n")
        for row in matrix:
            result.append(",".join(row) + "\n")

    # Simpan kembali ke file
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(result)  

def main():
    global baris, kolom
    
    tipe = None

    while (tipe == None):
        jadwalFilm.jadwal_Film()
        
        id_film = int(input('\nPilih ID film yang ingin ditonton: '))
        tipe = ambil_tipe_dari_id(id_film)
        print("\n---------------------------------------------------------------------------------------------------------------------------\n")

    ambil_ukuran_dari_tipe(tipe)
    matrix_kursi_tampilan = deklarasiMatriks(baris, kolom)
    matrix_kondisi_kursi = deklarasiMatriks(baris, kolom)
    
    # Simpan state kursi dari state_tempat_duduk.csv
    matrix_kondisi_kursi = ambil_state_kursi(id_film)
    
    # Simpan alfabet baris untuk tampilan
    matrix_kursi_tampilan = isiAlfabetMatriks(baris, kolom)

    # Simpan angka kolom untuk tampilan 
    for i in range(0, baris, 1):
        for j in range(0, kolom, 1):
            if (j+1 < 10):
                matrix_kursi_tampilan[i][j] += '0' + str(j+1)
            else:
                matrix_kursi_tampilan[i][j] += str(j+1)

    daftar_order = ''
    tiket = 0
    order = ''
    while (order != 'end'):
        err = False
        selesai = False
        i=0
        # tampilan tempat duduk, i = indeks baris, j = indeks kolom
        while ((not selesai) and (i < baris)):
            j = 0
            while ((not selesai) and (j < kolom)):
                if (order == matrix_kursi_tampilan[i][j]):
                    if (matrix_kondisi_kursi[i][j] != 'X'):
                        matrix_kondisi_kursi[i][j] = 'X'
                        daftar_order += order + ', '
                        tiket += 1    
                        selesai = True
                        print('Pesanan berhasil!\n')
                    else:
                        print('Maaf tempat duduk tersebut sudah dipesan!')
                        err = True
                j += 1
            i += 1
        if (not err and not selesai and order != ''):
            print('Maaf tempat duduk tersebut tidak tersedia!')
            err = True
            
        # tampilan tempat duduk, i = indeks baris, j = indeks kolom
        if (not err):
            for i in range(0, baris*3+1, 1):
                if (i == 0):
                    print(end='┌')
                    for j in range(0, kolom, 1):
                        if (j==kolom-1):
                            print('-----', end='┐')
                        else:
                            print('-----', end='┬')
                elif (i%3 == 1):
                    print(end='| ')
                    for j in range(0, kolom, 1):
                        print(matrix_kursi_tampilan[i//3][j], end=' | ')
                elif (i%3 == 2):
                    print(end='|  ')
                    for j in range(0, kolom, 1):
                        print(matrix_kondisi_kursi[i//3][j], end='  |  ')
                elif (i == baris*3):
                    print(end='└')
                    for j in range(0, kolom, 1):
                        if (j==kolom-1):
                            print('-----', end='┘')
                        else:
                            print('-----', end='┴')
                else:
                    print(end='├')
                    for j in range(0, kolom, 1):
                        if (j==kolom-1):
                            print('-----', end='┤')
                        else:
                            print('-----', end='┼')
                print()
            
        order = str(input('\nPesan tempat duduk (pilih nomor kursi yang belum dipesan, bila selesai ketik "end"): '))
        if (order == 'end'):
            daftar_order += order
        print()
        for j in range(0, (kolom * 6) + 10, 1):
            print(end='=')
        print('\n')

    simpan_state_kursi(id_film, matrix_kondisi_kursi)

    # pindahhin data films.csv yang diperlukan ke seats.csv
    with open('films.csv', mode='r', encoding='utf-8') as film:
        next(film)  # Lewati baris "List Jadwal Film"
        reader = csv.DictReader(film)
        for row in reader:
            if int(row['ID']) == id_film:
                judul = row['Judul']
                studio = row['Studio']

    with open("seats.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # simpan data dari file ini ke seats.csv
        writer.writerow(['Judul film'])
        writer.writerow([judul])
        writer.writerow([])
        writer.writerow(['Studio'])
        writer.writerow([studio])
        writer.writerow([])
        writer.writerow(['daftar tempat duduk'])
        writer.writerow([daftar_order])
        writer.writerow([])
        writer.writerow(['tipe bioskop'])
        writer.writerow([tipe])
        writer.writerow([])
        writer.writerow(['jumlah tiket'])
        writer.writerow([tiket])
        writer.writerow([])
    return 0

if __name__ == '__main__':    
    baris = 0
    kolom = 0
    main()