def main():
    # Setup tampilan
    baris = 10  # max 26 huruf 
    kolom = 15  # max 2 digit 
    arr_baris = baris * [None]
    arr_kolom = kolom * [None]
    arr_kolom_unavailable = [0, 7]
    arr_baris_unavailable = [1,2,3,4,5,6,7,8,9]
    
    # Simpan angka kolom versi tampilan 
    for i in range(0, kolom, 1):
        if (i+1 < 10):
            arr_kolom[i] = '0' + str(i+1)
        else:
            arr_kolom[i] = str(i+1)
            
    # Konversi angka menjadi alfabet dan simpan untuk versi tampilan 
    for i in range(0, baris, 1):
        if (i+1 == 1):
            arr_baris[i] = 'A'
        elif (i+1 == 2):
            arr_baris[i] = 'B'
        elif (i+1 == 3):
            arr_baris[i] = 'C'
        elif (i+1 == 4):
            arr_baris[i] = 'D'
        elif (i+1 == 5):
            arr_baris[i] = 'E'
        elif (i+1 == 6):
            arr_baris[i] = 'F'
        elif (i+1 == 7):
            arr_baris[i] = 'G'
        elif (i+1 == 8):
            arr_baris[i] = 'H'
        elif (i+1 == 9):
            arr_baris[i] = 'I'
        elif (i+1 == 10):
            arr_baris[i] = 'J'
        elif (i+1 == 11):
            arr_baris[i] = 'K'
        elif (i+1 == 12):
            arr_baris[i] = 'L'
        elif (i+1 == 13):
            arr_baris[i] = 'M'
        elif (i+1 == 14):
            arr_baris[i] = 'N'
        elif (i+1 == 15):
            arr_baris[i] = 'O'
        elif (i+1 == 16):
            arr_baris[i] = 'P'
        elif (i+1 == 17):
            arr_baris[i] = 'Q'
        elif (i+1 == 18):
            arr_baris[i] = 'R'
        elif (i+1 == 19):
            arr_baris[i] = 'S'
        elif (i+1 == 20):
            arr_baris[i] = 'T'
        elif (i+1 == 21):
            arr_baris[i] = 'U'
        elif (i+1 == 22):
            arr_baris[i] = 'V'
        elif (i+1 == 23):
            arr_baris[i] = 'W'
        elif (i+1 == 24):
            arr_baris[i] = 'X'
        elif (i+1 == 25):
            arr_baris[i] = 'Y'
        elif (i+1 == 26):
            arr_baris[i] = 'Z'
    
    # j = indeks baris, i = indeks kolom
    for j in range(0, baris*3+1, 1):
        if (j == 0):
            print(end='┌')
            for i in range(0, kolom, 1):
                if (i==kolom-1):
                    print('-----', end='┐')
                else:
                    print('-----', end='┬')
        elif (j%3 == 1):
            print(end='| ')
            for i in range(0, kolom, 1):
                unavailable = False
                for k in range(0, len(arr_kolom_unavailable), 1):
                    if (i == arr_kolom_unavailable[k]):
                        for l in range(0, len(arr_baris_unavailable), 1):
                            if(j//3 == arr_baris_unavailable[l]):
                                unavailable = True
                if(unavailable):
                    print('   ', end=' | ')
                else:
                    print(f'{arr_baris[j//3]}{arr_kolom[i]}', end=' | ')
        elif (j%3 == 2):
            print(end='| ')
            for i in range(0, kolom, 1):
                unavailable = False
                for k in range(0, len(arr_kolom_unavailable), 1):
                    if (i == arr_kolom_unavailable[k]):
                        for l in range(0, len(arr_baris_unavailable), 1):
                            if(j//3 == arr_baris_unavailable[l]):
                                unavailable = True
                if(unavailable):
                    print('   ', end=' | ')
                else:
                    print(' ✓ ', end=' | ')
        elif (j == baris*3):
            print(end='└')
            for i in range(0, kolom, 1):
                if (i==kolom-1):
                    print('-----', end='┘')
                else:
                    print('-----', end='┴')
        else:
            print(end='├')
            for i in range(0, kolom, 1):
                if (i==kolom-1):
                    print('-----', end='┤')
                else:
                    print('-----', end='┼')
        print()
        
    

    return 0

if __name__ == '__main__':    
    main()   