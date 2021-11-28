
l=[1,2,3,4,5]
# l Sebagai list
# Akses list
print("list=[1,2,3,4,5]")
print("Contoh Akses List")
print("Tampilkan Element ke 3 : ",l[2])
print("Tampilkan Element ke 2-4 : ",l[1:4])
print("Tampilkan Element Terakhir : ",l[5-1])

# Ubah Elemen List
print("Contoh Ubah Elemen List")
l[3]=8
print("Mengubah elemen ke 4 dengan nilai lainya :",l)
l[3:]=6,7
print("Mengubah elemen ke 4 sampai akhir dengan nilai lainya :",l)

# Tambah Elemen List
A=[0,1,2,3,4,]
B=[5,6,7,8,9]

print("Contoh Tambah Elemen List")
print("A=[0,1,2,3,4,]")
print("B=[5,6,7,8,9]")
# Pengabungan sebelum menggunakan append dan extend
C = A+B

B.extend(A[1:3])
print("2 bagian list A di jadikan list B",B)

B.append("lima")
print("Tambah list B dengan nilai string",B)

B.extend([10,11,12])
print("Tambah list B dengan 3 nilai",B)

print("Gabungan antara list A dan B",C)
C = A+B
# Pengabungan sesudah menggunakan append dan extend
print("Gabungan antara list A dan B setelah menggunakan append dan extend",C)