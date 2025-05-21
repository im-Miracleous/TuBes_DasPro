def main():
    # Setup tampilan
    baris = 14
    kolom = 14
    arr_baris = baris * [None]
    arr_kolom = kolom * [None]
    
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
    
    for j in range(0, baris*2, 1):
        if (j%2 == 1):
            print(end='| ')
            for i in range(0, kolom, 1):
                print(F'{arr_baris[j//2]}{arr_kolom[i]}', end=' | ')
        else:
            print(end='|')
            for i in range(0, kolom, 1):
                print('-----', end='|')
        print()
        
    

    return 0

if __name__ == '__main__':    
    main()   