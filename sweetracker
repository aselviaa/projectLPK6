# gula_tracker.py

def tampilkan_menu():
    print("\n=== APLIKASI PENGHITUNG GULA HARIAN ===")
    print("1. Tambah Produk")
    print("2. Lihat Daftar Produk")
    print("3. Hapus Produk")
    print("4. Lihat Total Gula")
    print("5. Keluar")

def tambah_produk(data):
    nama = input("Nama produk: ")
    try:
        gula = float(input("Kadar gula (gram): "))
        data.append({'nama': nama, 'gula': gula})
        print(f"✅ Produk '{nama}' ditambahkan.")
    except ValueError:
        print("❌ Input gula harus berupa angka.")

def tampilkan_daftar(data):
    if not data:
        print("🚫 Belum ada produk yang ditambahkan.")
        return
    print("\n--- Daftar Produk ---")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['nama']} - {item['gula']} gram")

def hapus_produk(data):
    tampilkan_daftar(data)
    if not data:
        return
    try:
        idx = int(input("Masukkan nomor produk yang ingin dihapus: "))
        if 1 <= idx <= len(data):
            produk = data.pop(idx - 1)
            print(f"🗑️ Produk '{produk['nama']}' dihapus.")
        else:
            print("❌ Nomor tidak valid.")
    except ValueError:
        print("❌ Input harus berupa angka.")

def hitung_total(data):
    total = sum(item['gula'] for item in data)
    print(f"📊 Total gula hari ini: {total} gram")

def main():
    data_produk = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        if pilihan == '1':
            tambah_produk(data_produk)
        elif pilihan == '2':
            tampilkan_daftar(data_produk)
        elif pilihan == '3':
            hapus_produk(data_produk)
        elif pilihan == '4':
            hitung_total(data_produk)
        elif pilihan == '5':
            print("👋 Keluar dari aplikasi. Tetap sehat!")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
