# Fungsi List
nama =[]
nim =[]
tugas =[]
uts =[]
uas =[]
akhir =[]
i=0
    # Fungsi i=0 untuk membuat titik respawn(kembali saat memilih Y)

while True:
        # variabel i... untuk menandakan command input

    inama=input("Nama   : ")
    nama.append(inama)
    inim=input("NIM : ")
    nim.append(inim)
    itugas=input("Nilai Tugas   : ")
    tugas.append(itugas)
    iuts=input("Nilai UTS   : ")
    uts.append(iuts)
    iuas=input("Nilai UAS   : ")
    uas.append(iuas)
    iakhir=(int(itugas)*0.30)+(int(iuts)*0.35)+(int(iuas)*0.35)
    akhir.append(iakhir)

        # Fungsi command Y/T
    i+=1
    ulang = input("ingin tambah data? y/t ")
    if ulang=="y":
        continue
    else:
        print("\n")
        break
        
        # Membuat bentuk border di hasil program
print("|------------------------------------------------------------------------------------------------|")
print("|                                        Daftar Mahasiswa                                        |")
print("|  No   |   Nama   |    NIM    |      TUGAS     |      UTS      |      UAS      |     Akhir      |")
print("|------------------------------------------------------------------------------------------------|")
for n in range(i):
    print("| ",n+1,"   |  ",nama[n],"  |  ",nim[n],"    |      ",tugas[n],"      |      ",uts[n],"     |     ",uas[n],"      |    "
    ,akhir[n],"      |")
    print("|------------------------------------------------------------------------------------------------|")