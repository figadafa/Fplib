from fplib import (ambil, jumlah, rata_rata, tambah, urutkan,
                   kelompokkan, peringkat, format_rupiah)

DATA = [
    {"nama": "Budi", "nilai": 80, "kelas": "A"},
    {"nama": "Sari", "nilai": 90, "kelas": "B"},
    {"nama": "Andi", "nilai": 70, "kelas": "A"},
]


def test_ambil():
    assert ambil("nama", DATA) == ["Budi", "Sari", "Andi"]


def test_jumlah():
    assert jumlah([1, 2, 3]) == 6
    assert jumlah([]) == 0


def test_rata_rata():
    assert rata_rata([80, 90, 70]) == 80
    assert rata_rata([]) == 0


def test_tambah_tidak_mengubah_asal():
    asal = [1, 2]
    hasil = tambah(asal, 3)
    assert hasil == [1, 2, 3]
    assert asal == [1, 2]


def test_urutkan():
    assert ambil("nama", urutkan("nilai", DATA)) == ["Andi", "Budi", "Sari"]
    assert ambil("nama", urutkan("nilai", DATA, menurun=True)) == ["Sari", "Budi", "Andi"]


def test_kelompokkan():
    grup = kelompokkan("kelas", DATA)
    assert ambil("nama", grup["A"]) == ["Budi", "Andi"]
    assert ambil("nama", grup["B"]) == ["Sari"]


def test_peringkat():
    hasil = peringkat("nilai", DATA)
    assert {d["nama"]: d["peringkat"] for d in hasil} == {"Sari": 1, "Budi": 2, "Andi": 3}


def test_format_rupiah():
    assert format_rupiah(15000) == "Rp 15.000"
    assert format_rupiah(0) == "Rp 0"