# Dokumentasi fplib

Dokumen ini menjelaskan library `fplib.py`, fungsi-fungsi di dalamnya, aplikasi yang memakainya, dan cara menjalankan serta mengujinya.

## 1. Daftar Fungsi

| Fungsi | Parameter | Hasil | Keterangan |
|---|---|---|---|
| `ambil(kunci, daftar)` | str, list of dict | list | Mengambil nilai satu field dari setiap item |
| `jumlah(angka)` | iterable angka | number | Menjumlahkan semua angka dengan `reduce` |
| `rata_rata(angka)` | iterable angka | float | Rata-rata, mengembalikan 0 jika kosong |
| `tambah(daftar, item)` | list, any | list | Mengembalikan list baru dengan item di akhir, list asal tidak berubah |
| `urutkan(kunci, daftar, menurun=False)` | str, list of dict, bool | list | Mengurutkan list berdasarkan field, list asal tidak berubah |
| `kelompokkan(kunci, daftar)` | str, list of dict | dict | Mengelompokkan item ke dalam dict of list berdasarkan field |
| `peringkat(kunci, daftar)` | str, list of dict | list | Menambahkan field `peringkat` (1 = nilai tertinggi) |
| `format_rupiah(n)` | number | str | Mengubah angka menjadi format rupiah, contoh `Rp 15.000` |

## 2. Prinsip Pemrograman Fungsional

- **Fungsi murni**: semua fungsi di `fplib.py` hanya bergantung pada input-nya dan tidak mengubah data dari luar.
- **Immutability**: `tambah`, `urutkan`, dan `peringkat` mengembalikan data baru, data asal tetap utuh. Dibuktikan oleh `test_tambah_tidak_mengubah_asal`.
- **Higher-order function**: `reduce`, `sorted` dengan `key`, dan lambda dipakai untuk memproses data.
- **Pemisahan I/O**: `input()` dan `print()` hanya ada di fungsi `main()` dan fungsi pembantu input di tiap aplikasi. Logika perhitungan berada di fplib.

## 3. Matriks Fungsi × Aplikasi

| Fungsi | Kasir Kantin | Presensi Kelas | Perpustakaan Mini | Keuangan Pribadi | Nilai Mahasiswa | Jumlah App |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `ambil` | ✅ | ✅ | ✅ | ✅ | ✅ | 5 |
| `jumlah` | ✅ | ✅ | ✅ | ✅ | | 4 |
| `rata_rata` | | ✅ | | ✅ | ✅ | 3 |
| `tambah` | ✅ | ✅ | ✅ | ✅ | | 4 |
| `urutkan` | ✅ | | | ✅ | ✅ | 3 |
| `kelompokkan` | | ✅ | ✅ | ✅ | | 3 |
| `peringkat` | | ✅ | ✅ | | ✅ | 3 |
| `format_rupiah` | ✅ | | ✅ | ✅ | | 3 |

Catatan: matriks ini harus dicek ulang setelah app temanmu final. Pastikan setiap fungsi dipakai di minimal 3 app.

## 4. Aplikasi

### Kasir Kantin (`app_kasir_kantin.py`)
- **Input**: nama menu yang diketik pengguna, dikosongkan untuk selesai.
- **Proses**: mencocokkan nama dengan daftar menu, lalu menambahkannya ke keranjang dengan `tambah`.
- **Output**: menu urut harga dengan `urutkan`, struk pesanan, dan total dengan `jumlah` dan `format_rupiah`.

### Presensi Kelas (`app_presensi_kelas.py`)
- **Input**: nama mahasiswa dan status hadir (1 atau 0), dikosongkan untuk selesai.
- **Proses**: mengelompokkan catatan per mahasiswa dengan `kelompokkan`, lalu menghitung total hadir dengan `jumlah`.
- **Output**: rata-rata hadir dengan `rata_rata` dan peringkat dengan `peringkat`.

### Perpustakaan Mini (`app_perpustakaan_mini.py`)
- Dikerjakan oleh Dicky. Isi bagian ini setelah app final.

### Keuangan Pribadi (`app_keuangan_pribadi.py`)
- Dikerjakan oleh Dicky. Isi bagian ini setelah app final.

### Nilai Mahasiswa (`app_nilai_mahasiswa.py`)
- Dikerjakan oleh Dicky. Isi bagian ini setelah app final.

## 5. Cara Menjalankan

```bash
pip install -r requirements.txt
pytest -v
python app_kasir_kantin.py
python app_presensi_kelas.py
```

## 6. Pengujian

`test_fplib.py` berisi 8 test untuk fungsi di `fplib.py`. Semua test lolos dengan perintah `pytest -v`.

Perlu dicatat: `DATA_DEMO` dan `PESANAN_DEMO` dipakai saat tidak ada input (misalnya di CI), sehingga aplikasi tetap bisa dijalankan tanpa keyboard.