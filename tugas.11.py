import datetime
import os
import random
import string

# Template dictionary untuk data buku
buku_template = {
    'judul': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0000,
    'terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA',
}

# Dictionary utama (Nesting Dictionary) untuk menyimpan seluruh data buku
data_perpustakaan = {}

while True:
  # Membersihkan layar terminal ('cls' untuk Windows, 'clear' untuk Linux/Mac)
  os.system('cls' if os.name == 'nt' else 'clear')

  print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^45}")
  print(f"{'INPUT DATA BUKU BARU':^45}")
  print('-' * 45)

  # Membuat dictionary baru dari keys template
  buku = dict.fromkeys(buku_template.keys())

  # Input data buku dari pengguna
  buku['judul'] = input('Judul Buku\t\t\t: ')
  buku['penulis'] = input('Penulis\t\t\t\t: ')
  buku['tahun_terbit'] = int(input('Tahun Terbit (YYYY)\t\t: '))

  print('\n--- Tanggal Terakhir Pinjam ---')
  tahun_pinjam = int(input('Tahun Pinjam (YYYY)\t\t: '))
  bulan_pinjam = int(input('Bulan Pinjam (1-12)\t\t: '))
  tanggal_pinjam = int(input('Tanggal Pinjam (1-31)\t\t: '))
  buku['terakhir_pinjam'] = datetime.datetime(
      tahun_pinjam, bulan_pinjam, tanggal_pinjam
  )

  status_input = input('Status (1: TERSEDIA / 2: TIDAK)\t: ')
  buku['status'] = 'TERSEDIA' if status_input == '1' else 'TIDAK'

  # Membuat Multi-Keys menggunakan Tuple: (KODE_ACAK, TAHUN_TERBIT)
  kode_acak = ''.join(random.choice(string.ascii_uppercase) for i in range(4))
  KEY = (kode_acak, buku['tahun_terbit'])

  # Memasukkan dictionary buku ke dalam dictionary utama (Nesting)
  data_perpustakaan.update({KEY: buku})

  # Menampilkan tabel daftar buku
  print('\n' + '=' * 95)
  print(
      f"{'KEYS':<15} {'JUDUL BUKU':<22} {'PENULIS':<18} {'TAHUN':<7}"
      f" {'TERAKHIR PINJAM':<17} {'STATUS':<10}"
  )
  print('=' * 95)

  for key in data_perpustakaan:
    # Mengubah format tuple key menjadi string agar rapi saat dicetak
    key_str = f'{key[0]}-{key[1]}'
    judul = data_perpustakaan[key]['judul']
    penulis = data_perpustakaan[key]['penulis']
    tahun = data_perpustakaan[key]['tahun_terbit']
    tgl_pinjam = data_perpustakaan[key]['terakhir_pinjam'].strftime('%x')
    status = data_perpustakaan[key]['status']

    print(
        f'{key_str:<15} {judul:<22} {penulis:<18} {tahun:<7} {tgl_pinjam:<17}'
        f' {status:<10}'
    )

  print('=' * 95 + '\n')

  lanjut = input('Apakah ingin menambah buku lagi (y/n)? ').lower()
  if lanjut == 'n':
    break

print('\nProgram selesai. Terima kasih telah menggunakan sistem perpustakaan!')