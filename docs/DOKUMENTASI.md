# Dokumentasi fplib

## Daftar Fungsi

| Fungsi | Parameter | Keterangan |
|---|---|---|
| `ambil(kunci, daftar)` | str, list of dict | Ambil nilai satu field dari setiap item |
| `jumlah(angka)` | iterable | Jumlahkan semua angka (pakai `reduce`) |
| `rata_rata(angka)` | iterable | Rata-rata, 0 jika kosong |
| `tambah(daftar, item)` | list, any | Kembalikan list baru dengan item di akhir |
| `urutkan(kunci, daftar, menurun=False)` | str, list of dict, bool | Urutkan berdasarkan field |
| `kelompokkan(kunci, daftar)` | str, list of dict | Kelompokkan menjadi dict of list |
| `peringkat(kunci, daftar)` | str, list of dict | Tambahkan field `peringkat` (1 = tertinggi) |
| `format_rupiah(n)` | number | Format ke "Rp 15.000" |

## Matriks Fungsi × Aplikasi

Syarat tugas: setiap fungsi dipakai minimal 3 dari 5 aplikasi.

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

## Cara Menjalankan

```bash
pip install -r requirements.txt
pytest -v                       # jalankan test
python app_kasir_kantin.py      # jalankan salah satu aplikasi
```

## Prinsip Pemrograman Fungsional

- **Pure function**: output hanya bergantung pada input.
- **Immutability**: data asal tidak diubah, fungsi mengembalikan data baru.
- **Higher-order function**: `reduce`, `sorted` dengan `key`, dan generator dipakai untuk memproses data.