#List Kendaraan 
Kendaraan = ["Motor", "Mobil", "Sepeda", "Bus"]
print(f"Data awal = {Kendaraan}")

# a menambahkan 'truk' di akhir list 
Kendaraan.append("truk")
print(f"a. setelah di tambah truk = {Kendaraan}")

# b menyisipkan 'becak' pada index ke-1
Kendaraan.insert(1, "becak")
print(f"b. setelah disisipkan becak = {Kendaraan}")

# c menghapus data paling belakang
Kendaraan.pop()
print(f"c. setelah data terakhir dihapus = {Kendaraan}" )

# d mengubah 'sepeda' menjadi 'skuter' 
Kendaraan[3] = "skuter"
print(f"d. setelah sepeda diubah menjadi skuter = {Kendaraan}")

# e menampilkan jumlah total data 
jumlah_data = len (Kendaraan)
print(f"e. jumlah total data = {jumlah_data}")

# SOAL 2 

# List nilai siswa
angka = [75 , 80, 90, 75, 85, 100, 65]
print(f"data nilai siswa = {angka}")

# a mencari index skor 100
index_100 = angka.index (100)
print(f"a. index skor 100 = {index_100}")

# b jumlah siswa yang 75
skor_75 = angka.count(75)
print(f"b. siswa yang mendaoatkan skor 75 ada ={skor_75}")

# c mengurutkan nilai dari kecil hingga besar 
angka.sort()
print(f"c. Mengurutkan data kecil kebesar = {angka}")

# d membalikan nilai dari terbesar ke terkecil 
angka.reverse()
print(f"d. membalikan nilai dari terbesar ke terkecil = {angka}")

# Soal 3
menu_utama = ["Nasi Goreng", "Mie ayam"]
menu_tambahan = ["kerupuk", "Es teh"]

#menggabukan menu tambah ke menu utama dan menampilkan hasil gabungan
menu_utama.extend(menu_tambahan)
print(f"menu utama setelah digabungkan = {menu_utama}")

# Soal 4
# Data barang dan harga
data_barang = [
    ["Buku", 5000],
    ["Pensil", 2000],
    ["Penggaris", 3000]
]

# a menampilkan harga pensil
harga_pensil = data_barang[1][1]
print(f"a. harga pensil = {harga_pensil}")

# b menampilkan semua data dengan perulangan for
print("b. data barang : ")

for barang in data_barang :
    print(barang)