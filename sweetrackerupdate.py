# gula_tracker_otomatis.py

# Daftar produk dan kadar gula dalam gram per porsi
produk_gula = {
    "aqua": 0.0,
    "teh botol": 18.0,
    "coca cola": 35.0,
    "sprite": 33.0,
    "oreo": 8.0,
    "ultra milk": 10.5,
    "nutrisari": 20.0,
    "indomilk": 12.0,
    "fanta": 36.0,
    "good day": 17.0
}

def tampilkan_menu():
    print("\n=== GulaTracker Otomatis ===")
    print("1. Tambah Produk")
    print("2. Lihat Daftar Konsumsi")
    print("3. Hapus Produk")
    print("4. Lihat Total Gula")
    print("5. Lihat Daftar Produk Tersedia")
    print("6. Keluar")

def tambah_produk(data):
    nama = input("Nama produk: ").lower()
    if nama in produk_gula:
        gula = produk_gula[nama]
        data.append({'nama': nama, 'gula': gula})
        print(f"✅ '{nama.title()}' ditambahkan ({gula} gram gula).")
    else:
        print(f"❌ Produk '{nama}' tidak ada dalam database.")

def tampilkan_daftar(data):
    if not data:
        print("🚫 Belum ada konsumsi hari ini.")
        return
    print("\n--- Daftar Konsumsi Hari Ini ---")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['nama'].title()} - {item['gula']} gram")

def hapus_produk(data):
    tampilkan_daftar(data)
    if not data:
        return
    try:
        idx = int(input("Nomor produk yang ingin dihapus: "))
        if 1 <= idx <= len(data):
            produk = data.pop(idx - 1)
            print(f"🗑️ Produk '{produk['nama'].title()}' dihapus.")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Masukkan angka yang benar.")

def hitung_total(data):
    total = sum(item['gula'] for item in data)
    print(f"📊 Total gula hari ini: {total} gram")

def tampilkan_database_produk():
    print("\n📋 Daftar Produk dalam Database:")
    for nama, gula in produk_gula.items():
        print(f"- {nama.title()} : {gula} gram")

def main():
    data_konsumsi = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            tambah_produk(data_konsumsi)
        elif pilihan == '2':
            tampilkan_daftar(data_konsumsi)
        elif pilihan == '3':
            hapus_produk(data_konsumsi)
        elif pilihan == '4':
            hitung_total(data_konsumsi)
        elif pilihan == '5':
            tampilkan_database_produk()
        elif pilihan == '6':
            print("👋 Terima kasih! Tetap sehat & batasi gula ya.")
            break
        else:
            print("❌ Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()
