# 1 TUPlE DAN SET

Mahasiswa = ("Azkandytad Davia Nusa Satrya", "2605060066", "Teknologi Informasi")
print("Data Mahasiswa:", Mahasiswa)

print("NIM:", Mahasiswa[1])
print("Program Studi:", Mahasiswa[2])

nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Nilai Angka:", nilai_angka)

# 2 Manipulasi Dictionary
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}

print("Data Awal:", data_mahasiswa)

data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026

print("Setelah Diubah:", data_mahasiswa)

del data_mahasiswa["nim"]
print("Data Mahasiswa Akhir:", data_mahasiswa)

# 3 Perulangan pada Dicitionary
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print(" Daftar Harga Buah ")

for barang, harga in keranjang.items():
    print(f"Harga {barang}: Rp {harga}")
    

total_belanja = 0

for harga in keranjang.values():
    total_belanja += harga

print("Total Belanja: Rp", total_belanja)