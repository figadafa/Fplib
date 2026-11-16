# fplib

Library Python bergaya **pemrograman fungsional** untuk tugas mata kuliah
Pemrograman Fungsional, Informatika UMM.

## Anggota Kelompok

| Nama | NIM | Tugas |
|---|---|---|
| Figa Brilliant Daffa | 202410370110424 | fplib.py, test, App 1-2 |
| Dicky Ihsan Novanda | 202410370110426| App 3-5, dokumentasi |

## Isi Repositori

- `fplib.py` - library utama (8 fungsi)
- `test_fplib.py` - unit test dengan pytest
- `app_*.py` - 5 aplikasi yang memakai library
- `docs/DOKUMENTASI.md` - daftar fungsi dan matriks penggunaan
- `.github/workflows/ci.yml` - CI otomatis menjalankan test dan semua aplikasi

## Persyaratan

- Python 3.9+
- pytest (lihat `requirements.txt`)

## Instalasi

```bash
git clone https://github.com/USERNAME/fplib-umm.git
cd fplib-umm
pip install -r requirements.txt
```

## Menjalankan

```bash
pytest -v                      # test library
python app_kasir_kantin.py
python app_presensi_kelas.py
python app_perpustakaan_mini.py
python app_keuangan_pribadi.py
python app_nilai_mahasiswa.py
```

## Contoh Penggunaan

```python
from fplib import ambil, jumlah, format_rupiah

harga = ambil("harga", [{"harga": 15000}, {"harga": 4000}])
print(format_rupiah(jumlah(harga)))   # Rp 19.000
```

## Aplikasi yang Menggunakan fplib

| Aplikasi | File | Fungsi yang dipakai |
|---|---|---|
| Kasir Kantin | `app_kasir_kantin.py` | ambil, jumlah, tambah, urutkan, format_rupiah |
| Presensi Kelas | `app_presensi_kelas.py` | ambil, jumlah, kelompokkan, peringkat, tambah, rata_rata |
| Perpustakaan Mini | `app_perpustakaan_mini.py` | ambil, jumlah, kelompokkan, peringkat, tambah, format_rupiah |
| Keuangan Pribadi | `app_keuangan_pribadi.py` | ambil, jumlah, kelompokkan, rata_rata, tambah, urutkan, format_rupiah |
| Nilai Mahasiswa | `app_nilai_mahasiswa.py` | ambil, rata_rata, peringkat, urutkan |

Detail lengkap ada di [docs/DOKUMENTASI.md](docs/DOKUMENTASI.md).