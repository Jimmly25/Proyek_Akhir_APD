from prettytable import PrettyTable

data_pemain = {}  

def tambah_pemain():
    print("\n=== TAMBAH PEMAIN ===")

    while True:
        nama = input("Nama pemain: ").strip()
        if nama:
            break
        print("❌ Nama tidak boleh kosong!")

    while True:
        umur_in = input("Umur pemain: ").strip()
        try:
            umur = int(umur_in)
            if umur > 0:
                break
            print("❌ Umur harus lebih dari 0!")
        except ValueError:
            print("❌ Umur harus angka!")

    while True:
        tgl = input("Tanggal lahir (dd-mm-yyyy): ").strip()
        try:
            d, m, y = map(int, tgl.split("-"))
            break
        except:
            print("❌ Format tanggal salah! Gunakan dd-mm-yyyy")

    while True:
        tim = input("Masukkan Nama TIM: ").strip()
        if tim:
            break
        print("❌ Tim tidak boleh kosong!")

    if tim not in data_pemain:
        data_pemain[tim] = {}

    while True:
        game = input("Game pemain: ").strip()
        if game:
            break
        print("❌ Game tidak boleh kosong!")

    while True:
        jk = input("Jenis kelamin (L/P): ").upper().strip()
        if jk in ("L", "P"):
            break
        print("❌ Masukkan L atau P!")

    data_pemain[tim][nama] = {
        "umur": umur,
        "tgl": tgl,
        "game": game,
        "jk": jk
    }

    print(f"✅ Pemain '{nama}' berhasil ditambahkan ke TIM '{tim}'!\n")


def cari_pemain():
    cari = input("Masukkan nama pemain: ").lower().strip()
    hasil = []

    for tim, pemain in data_pemain.items():
        for nama, p in pemain.items():
            if nama.lower() == cari:
                hasil.append((nama, tim, p["umur"], p["tgl"], p["game"], p["jk"]))

    if not hasil:
        print("❌ Pemain tidak ditemukan!\n")
        return

    print(f"\n=== HASIL PENCARIAN '{cari.upper()}' ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "TIM", "Umur", "Tanggal Lahir", "Game", "Jenis Kelamin"]

    for h in hasil:
        tabel.add_row(h)

    print(tabel)
    print()