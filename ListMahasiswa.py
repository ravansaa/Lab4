i=0
# Fungsi List
nama =[]
nim =[]
tugas =[]
uts =[]
uas =[]
akhir =[]
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

    more=""
    while more!="y" and more!="t":
        more=input("Tambah Data (y/t) ?")
    i+=1
    if more=="t":
        break

print("|                                        Daftar Mahasiswa                                        |")
print("|  No   |   Nama   |    NIM    |      TUGAS     |      UTS      |      UAS      |     Akhir      |")
print("|------------------------------------------------------------------------------------------------|")
for n in range(i):
    print("| ",n+1,"   |  ",nama[n],"  |  ",nim[n],"    |      ",tugas[n],"      |      ",uts[n],"     |     ",uas[n],"      |    "
    ,akhir[n],"      |")
print("|------------------------------------------------------------------------------------------------|")