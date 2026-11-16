from fplib import ambil, jumlah, kelompokkan, rata_rata, tambah, urutkan, format_rupiah


DATA_DEMO = [
    {"ket": "Gaji", "tipe": "masuk", "kategori": "Pekerjaan", "jumlah": 5000000},
    {"ket": "Makan", "tipe": "keluar", "kategori": "Kebutuhan", "jumlah": 25000},
    {"ket": "Transportasi", "tipe": "keluar", "kategori": "Transportasi", "jumlah": 15000},
]


def hitung_ringkasan(transaksi):
    masuk = [item for item in transaksi if item["tipe"] == "masuk"]
    keluar = [item for item in transaksi if item["tipe"] == "keluar"]
    total_masuk = jumlah(ambil("jumlah", masuk))
    total_keluar = jumlah(ambil("jumlah", keluar))
    per_kategori = kelompokkan("kategori", keluar)
    kategori_total = {k: jumlah(ambil("jumlah", v)) for k, v in per_kategori.items()}
    rata_keluar = rata_rata(ambil("jumlah", keluar))
    terbesar = urutkan("jumlah", transaksi, menurun=True)[0] if transaksi else None
    return total_masuk, total_keluar, kategori_total, rata_keluar, terbesar


def baca_transaksi_baru():
    try:
        ket = input("Keterangan (kosong untuk melewati): ").strip()
        if not ket:
            return None
        tipe = input("Tipe (masuk/keluar): ").strip().lower()
        if tipe not in ("masuk", "keluar"):
            return None
        kategori = input("Kategori: ").strip()
        nilai = int(input("Jumlah rupiah: "))
        return {"ket": ket, "tipe": tipe, "kategori": kategori, "jumlah": nilai}
    except (EOFError, ValueError):
        # Data demo dipakai jika input tidak tersedia atau tidak valid.
        return None


def main():
    transaksi = DATA_DEMO[:]
    transaksi_baru = baca_transaksi_baru()
    if transaksi_baru is not None:
        transaksi = tambah(transaksi, transaksi_baru)
    masuk, keluar, kategori, rata_keluar, terbesar = hitung_ringkasan(transaksi)
    print(f"\nTotal pemasukan: {format_rupiah(masuk)}")
    print(f"Total pengeluaran: {format_rupiah(keluar)}")
    print("Pengeluaran per kategori:")
    for nama, nilai in kategori.items():
        print(f"- {nama}: {format_rupiah(nilai)}")
    print(f"Rata-rata pengeluaran: {format_rupiah(rata_keluar)}")
    if terbesar:
        print(f"Transaksi terbesar: {terbesar['ket']} ({format_rupiah(terbesar['jumlah'])})")


if __name__ == "__main__":
    main()
