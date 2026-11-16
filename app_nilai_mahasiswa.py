from fplib import ambil, rata_rata, peringkat, urutkan


DATA_DEMO = [
    {"nama": "Ayu", "tugas": 80, "uts": 85, "uas": 90},
    {"nama": "Budi", "tugas": 75, "uts": 78, "uas": 80},
    {"nama": "Citra", "tugas": 92, "uts": 88, "uas": 95},
]


def tambah_nilai_akhir(daftar):
    """Menghasilkan data mahasiswa dengan nilai akhir."""
    hasil = []
    for mahasiswa in daftar:
        data = mahasiswa.copy()
        data["akhir"] = rata_rata([data["tugas"], data["uts"], data["uas"]])
        hasil.append(data)
    return hasil


def baca_mahasiswa_baru():
    try:
        nama = input("Nama mahasiswa (kosong untuk melewati): ").strip()
        if not nama:
            return None
        tugas = float(input("Nilai tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        return {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas}
    except (EOFError, ValueError):
        # Data demo dipakai saat tidak ada input dari pengguna.
        return None


def main():
    mahasiswa = DATA_DEMO[:]
    baru = baca_mahasiswa_baru()
    if baru is not None:
        mahasiswa.append(baru)
    mahasiswa = tambah_nilai_akhir(mahasiswa)

    print("\nNama urut abjad:", ", ".join(ambil("nama", urutkan("nama", mahasiswa))))
    print(f"Rata-rata nilai kelas: {rata_rata(ambil('akhir', mahasiswa)):.2f}")
    print("Peringkat mahasiswa:")
    for item in peringkat("akhir", mahasiswa):
        print(f"- {item['peringkat']}. {item['nama']}: {round(item['akhir'], 2):.2f}")


if __name__ == "__main__":
    main()
