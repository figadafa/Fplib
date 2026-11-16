from fplib import ambil, jumlah, kelompokkan, peringkat, tambah, rata_rata

# Data demo, dipakai kalau tidak ada input (misalnya saat CI)
DATA_DEMO = [
    {"nama": "Budi", "hadir": 1},
    {"nama": "Sari", "hadir": 1},
    {"nama": "Budi", "hadir": 0},
    {"nama": "Sari", "hadir": 1},
    {"nama": "Andi", "hadir": 1},
]


def ambil_catatan():
    # Kumpulkan catatan kehadiran dari pengguna sampai input kosong
    catatan = []
    try:
        while True:
            nama = input("Nama mahasiswa (kosongkan untuk selesai): ").strip()
            if nama == "":
                break
            hadir_str = input("  Hadir? (1 = hadir, 0 = tidak): ").strip()
            # Hanya terima angka 0 atau 1
            if hadir_str not in ("0", "1"):
                print("  Isi dengan 0 atau 1, catatan dilewati.")
                continue
            catatan = tambah(catatan, {"nama": nama, "hadir": int(hadir_str)})
            print(f"  + {nama} dicatat")
    except EOFError:
        # Dijalankan tanpa keyboard: pakai data demo
        return DATA_DEMO

    if len(catatan) == 0:
        return DATA_DEMO
    return catatan


def main():
    catatan = ambil_catatan()

    # Kelompokkan catatan per nama, lalu hitung total hadir tiap mahasiswa
    rekap = [
        {"nama": nama, "hadir": jumlah(ambil("hadir", rows))}
        for nama, rows in kelompokkan("nama", catatan).items()
    ]

    print()
    print("=== REKAP KEHADIRAN ===")
    print("Rata-rata hadir per mahasiswa:", round(rata_rata(ambil("hadir", rekap)), 2))
    for r in peringkat("hadir", rekap):
        print(f"{r['peringkat']}. {r['nama']} - {r['hadir']} kali hadir")


if __name__ == "__main__":
    main()