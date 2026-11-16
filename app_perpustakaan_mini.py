from fplib import ambil, jumlah, kelompokkan, peringkat, tambah, format_rupiah


DATA_DEMO = [
    {"judul": "Laskar Pelangi", "kategori": "Novel", "pinjam": 12, "hari_telat": 2},
    {"judul": "Bumi Manusia", "kategori": "Novel", "pinjam": 18, "hari_telat": 0},
    {"judul": "Python Dasar", "kategori": "Teknologi", "pinjam": 9, "hari_telat": 3},
]


def hitung_denda(daftar):
    """Menghitung denda setiap buku dan total seluruh denda."""
    denda = [buku["hari_telat"] * 1000 for buku in daftar]
    return denda, jumlah(denda)


def baca_buku_baru():
    try:
        judul = input("Judul buku baru (kosong untuk melewati): ").strip()
        if not judul:
            return None
        kategori = input("Kategori: ").strip()
        pinjam = int(input("Jumlah kali dipinjam: "))
        hari_telat = int(input("Hari telat: "))
        return {"judul": judul, "kategori": kategori, "pinjam": pinjam, "hari_telat": hari_telat}
    except (EOFError, ValueError):
        # Data demo membuat program tetap berjalan tanpa keyboard.
        return None


def main():
    buku = DATA_DEMO[:]
    buku_baru = baca_buku_baru()
    if buku_baru is not None:
        buku = tambah(buku, buku_baru)

    print("\nJumlah buku per kategori:")
    for kategori, daftar in kelompokkan("kategori", buku).items():
        print(f"- {kategori}: {len(daftar)} judul")

    print("\n2 buku terpopuler:")
    for item in peringkat("pinjam", buku)[:2]:
        print(f"- {item['peringkat']}. {item['judul']} ({item['pinjam']} kali)")

    _, total_denda = hitung_denda(buku)
    print(f"\nTotal denda: {format_rupiah(total_denda)}")
    print("Semua judul:", ", ".join(ambil("judul", buku)))


if __name__ == "__main__":
    main()
