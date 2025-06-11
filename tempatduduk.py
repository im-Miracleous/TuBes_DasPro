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

def main():
    # Menu tipe bioskop
    tipe = jadwalFilm.tipe_bioskop()

    # Setup tampilan sesuai tipe bioskop
    if (tipe == "Reguler/Deluxe"):
        baris = 10  # max 26 huruf , 2D 10, 4DX 8
        kolom = 20  # max 2 digit , 2D 20, 4DX 16
    elif (tipe == "4DX"):
        baris = 8
        kolom = 16
    elif (tipe == "Premium"):
        baris = 5
        kolom = 6
    matrix_kursi_tampilan = deklarasiMatriks(baris, kolom)
    matrix_kondisi_kursi = deklarasiMatriks(baris, kolom)

    # Simpan state kursi 
    for i in range(0, baris, 1):
        for j in range(0, kolom, 1):
            matrix_kondisi_kursi[i][j] = ' V '
    
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
        for i in range(0, baris, 1):
            for j in range(0, kolom, 1):
                if (order == matrix_kursi_tampilan[i][j]):
                    matrix_kondisi_kursi[i][j] = ' X '
        # tampilan tempat duduk, i = indeks baris, j = indeks kolom
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
                print(end='| ')
                for j in range(0, kolom, 1):
                    print(matrix_kondisi_kursi[i//3][j], end=' | ')
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
            
        tiket = tiket + 1    
    
        order = str(input('\nPesan tempat duduk: '))
        print()
        for j in range(0, (kolom * 6) + 10, 1):
            print(end='=')
        print('\n')

        if (order != 'end'):
            daftar_order += order + ', '
        else:
            daftar_order += order

    with open("seats.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(['tipe bioskop'])
        writer.writerow([tipe])
        writer.writerow([])
        writer.writerow(['daftar tempat duduk'])
        writer.writerow([daftar_order])
        writer.writerow([])
        writer.writerow(['jumlah tiket'])
        writer.writerow([tiket-1])  # -1 karena 'end' tidak dihitung sebagai tiket
        writer.writerow([])
        writer.writerow(['state tempat duduk'])
        writer.writerows(matrix_kondisi_kursi)

    return 0

if __name__ == '__main__':    
    main()