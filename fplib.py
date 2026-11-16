"""
fplib.py - Library fungsi umum bergaya fungsional.
Semua fungsi bersifat pure: tidak mengubah data input, selalu mengembalikan data baru.
"""
from functools import reduce


def ambil(kunci, daftar):
    """Ambil nilai dari field `kunci` pada setiap dict dalam daftar."""
    return [item[kunci] for item in daftar]


def jumlah(angka):
    """Jumlahkan semua angka dalam iterable."""
    return reduce(lambda a, b: a + b, angka, 0)


def rata_rata(angka):
    """Rata-rata dari iterable angka. Mengembalikan 0 jika kosong."""
    angka = list(angka)
    return jumlah(angka) / len(angka) if angka else 0


def tambah(daftar, item):
    """Kembalikan daftar baru yang berisi item di akhir."""
    return [*daftar, item]


def urutkan(kunci, daftar, menurun=False):
    """Urutkan list of dict berdasarkan field `kunci`."""
    return sorted(daftar, key=lambda d: d[kunci], reverse=menurun)


def kelompokkan(kunci, daftar):
    """Kelompokkan list of dict berdasarkan field `kunci` menjadi dict of list."""
    def masuk_grup(acc, item):
        k = item[kunci]
        return {**acc, k: [*acc.get(k, []), item]}
    return reduce(masuk_grup, daftar, {})


def peringkat(kunci, daftar):
    """Tambahkan field 'peringkat' (1 = nilai tertinggi) berdasarkan `kunci`."""
    urut = urutkan(kunci, daftar, menurun=True)
    return [{**item, "peringkat": i} for i, item in enumerate(urut, start=1)]


def format_rupiah(n):
    """Format angka ke format rupiah, contoh: 15000 -> 'Rp 15.000'."""
    return "Rp {:,}".format(int(n)).replace(",", ".")