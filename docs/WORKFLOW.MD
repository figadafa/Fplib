# WORKFLOW

Panduan kerja untuk tugas Pemrograman Fungsional (fplib). Dokumen ini dibuat supaya siapa pun, termasuk AI yang membantu, bisa mengikuti alurnya tanpa bertanya ulang.

## Tujuan

Membuat 5 aplikasi Python yang memakai library `fplib.py`. Setiap aplikasi harus berjalan dengan `python nama_file.py` tanpa error.

## Pembagian Tugas

| Anggota | Branch | File yang dikerjakan |
|---|---|---|
| Figa Brilliant Daffa | `figa/library-app` | `fplib.py`, `test_fplib.py`, `docs/DOKUMENTASI.md`, `app_kasir_kantin.py`, `app_presensi_kelas.py` |
|Dicky Ihsan Novanda | `dicky/app-3-5` | `app_perpustakaan_mini.py`, `app_keuangan_pribadi.py`, `app_nilai_mahasiswa.py` |

**Aturan penting:**
- Jangan mengubah `fplib.py` kalau bukan file milikmu. Kalau fungsinya kurang, tanyakan dulu ke Figa.
- Jangan mengubah `README.md` dan `.github/workflows/ci.yml`. Kedua file itu hanya diubah oleh Figa.
- Nama file dan nama fungsi harus persis sama seperti di tabel dan di `fplib.py`.

## Langkah Kerja Dicky

### 1. Clone repo (sekali saja)

```bash
git clone https://github.com/figadafa/Fplib.git
cd Fplib
```

### 2. Pastikan `main` terbaru, lalu buat branch

```bash
git checkout main
git pull
git checkout -b dicky/app-3-5
```

Tunggu sampai Figa sudah merge PR-nya ke `main`, supaya `fplib.py` sudah ada. Cek dengan `ls fplib.py`.

### 3. Buat 3 file app

Buat file `app_perpustakaan_mini.py`, `app_keuangan_pribadi.py`, dan `app_nilai_mahasiswa.py` sesuai prompt yang sudah disiapkan. Simpan di folder yang sama dengan `fplib.py`.

### 4. Cek di komputer

```bash
python app_perpustakaan_mini.py
python app_keuangan_pribadi.py
python app_nilai_mahasiswa.py
```

Kalau ada error, kirim pesan errornya ke AI dan minta diperbaiki. Jangan ubah `fplib.py`.

### 5. Commit dengan nama sendiri

 commit dan push:

```bash
git add app_perpustakaan_mini.py app_keuangan_pribadi.py app_nilai_mahasiswa.py
git commit -m "Tambah app 3-5"
git push -u origin teman/app-3-5
```

### 6. Buat Pull Request

1. Buka repo di GitHub, lalu tab **Pull requests** → **New pull request**.
2. Base: `main`. Compare: `teman/app-3-5`.
3. Klik **Create pull request**, lalu beri tahu Figa.
4. Setelah Figa menyetujui, klik **Merge pull request**.

## Langkah Kerja Figa

1. Kerjakan di branch `figa/library-app`, lalu push.
2. Buat PR ke `main`, lalu merge.
3. Setelah PR teman masuk, jalankan:

```bash
git checkout main
git pull
pytest -v
```

4. Cek tab **Actions** di GitHub. Harus hijau.

## Cara Cek Hasil

- **Pull requests**: ada dua PR, masing-masing dari Figa dan teman.
- **Actions**: CI harus hijau dan menjalankan semua app.
- **Commits** di `main`: nama penulis tercatat untuk setiap commit.

## Kalau Ada Masalah

| Masalah | Solusi |
|---|---|
| `git push` ditolak | Jalankan `git pull` dulu, lalu push lagi |
| Konflik saat merge | Jangan tebak. Kirim pesan konfliknya ke Figa |
| App error | Kirim pesan error ke AI dan minta perbaikan, tanpa mengubah `fplib.py` |
| CI merah | Cek tab Actions, lihat langkah yang gagal, lalu beri tahu Figa |