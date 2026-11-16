from fplib import ambil, jumlah, tambah, urutkan, format_rupiah

# Menu kantin, minimal 10 item
MENU = [
    {"nama": "Nasi Goreng", "harga": 15000},
    {"nama": "Mie Ayam", "harga": 12000},
    {"nama": "Nasi Ayam Geprek", "harga": 13000},
    {"nama": "Bakso", "harga": 11000},
    {"nama": "Soto Ayam", "harga": 12000},
    {"nama": "Roti Bakar", "harga": 7000},
    {"nama": "Gorengan", "harga": 1000},
    {"nama": "Es Teh", "harga": 4000},
    {"nama": "Es Jeruk", "harga": 5000},
    {"nama": "Air Mineral", "harga": 3000},
]

# Pesanan demo dipakai kalau tidak ada input (misalnya saat CI)
PESANAN_DEMO = [MENU[0], MENU[7], MENU[9]]


def tampilkan_menu():
    # Urutkan menu dari harga termurah
    print("=== MENU KANTIN ===")
    for m in urutkan("harga", MENU):
        print(f"- {m['nama']}: {format_rupiah(m['harga'])}")
    print()


def ambil_pesanan():
    # Kumpulkan pesanan sampai pengguna mengosongkan input
    keranjang = []
    try:
        while True:
            nama = input("Ketik nama menu (kosongkan untuk selesai): ").strip()
            if nama == "":
                break
            # Cari menu yang namanya cocok (tidak peduli huruf besar/kecil)
            ditemukan = [m for m in MENU if m["nama"].lower() == nama.lower()]
            if ditemukan:
                keranjang = tambah(keranjang, ditemukan[0])
                print(f"  + {ditemukan[0]['nama']} ditambahkan")
            else:
                print("  Menu tidak ditemukan, coba ketik ulang.")
    except EOFError:
        # Dijalankan tanpa keyboard: pakai data demo
        return PESANAN_DEMO

    # Kalau tidak ada yang dipesan, pakai data demo
    if len(keranjang) == 0:
        return PESANAN_DEMO
    return keranjang


def main():
    tampilkan_menu()
    keranjang = ambil_pesanan()

    print()
    print("=== STRUK ===")
    for nama in ambil("nama", keranjang):
        print("-", nama)
    print("Jumlah item:", len(keranjang))
    print("Total belanja:", format_rupiah(jumlah(ambil("harga", keranjang))))


if __name__ == "__main__":
    main()