from prettytable import PrettyTable

data_pemain = {}  # data pemain per TIM

def tambah_pemain():
    print("\n=== TAMBAH PEMAIN ===")
    while True:
        nama = input("Nama pemain: ").strip()
        if nama: break
        print("❌ Nama tidak boleh kosong!")
    while True:
        umur_in = input("Umur pemain: ").strip()
        if umur_in.isdigit() and int(umur_in) > 0:
            umur = int(umur_in)
            break
        print("❌ Umur harus angka lebih dari 0!")
    while True:
        tgl = input("Tanggal lahir (dd-mm-yyyy): ").strip()
        bagian = tgl.split("-")
        if len(bagian) == 3 and all(x.isdigit() for x in bagian): break
        print("❌ Format salah!")
    while True:
        tim = input("Masukkan Nama TIM: ").strip()
        if tim: break
        print("❌ Tim tidak boleh kosong!")
    while True:
        jk = input("Jenis kelamin (L/P): ").upper().strip()
        if jk in ("L", "P"): break
        print("❌ Harus L atau P!")

    if tim not in data_pemain:
        data_pemain[tim] = {}

    data_pemain[tim][nama] = {"umur": umur, "tgl": tgl, "jk": jk}
    print(f"✅ Pemain '{nama}' berhasil ditambahkan ke TIM {tim}!\n")


def cari_pemain():
    # Cek apakah data pemain kosong
    if not data_pemain:
        print("\n❗ Belum ada pemain.\n")
        return

    cari = input("Masukkan nama pemain: ").lower().strip()

    hasil = []
    for tim, pemain in data_pemain.items():
        for nama, p in pemain.items():
            if nama.lower() == cari:
                hasil.append((nama, tim, p["umur"], p["tgl"], p["jk"]))

    if not hasil:
        print("❌ Pemain tidak ditemukan!\n")
        return

    print(f"\n=== HASIL PENCARIAN '{cari.upper()}' ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "TIM", "Umur", "Tanggal Lahir", "JK"]

    for h in hasil:
        tabel.add_row(h)

    print(tabel)
    print()

def lihat_pemain_berdasarkan_tim():
    if not data_pemain:
        print("\n❗ Belum ada Tim.\n")
        return

    tim = input("Masukkan nama TIM: ").strip()

    if tim not in data_pemain:
        print(f"❌ Tidak ada pemain dari TIM '{tim}'.\n")
        return

    print(f"\n=== TIM {tim.upper()} ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Umur", "Tanggal Lahir", "JK"]

    for nama, p in data_pemain[tim].items():
        tabel.add_row([nama, p["umur"], p["tgl"], p["jk"]])

    print(tabel)
    print()


def lihat_semua_pemain():
    if not data_pemain:
        print("\n❗ Belum ada pemain.\n")
        return
    for tim, pemain in data_pemain.items():
        print(f"\n=== TIM {tim.upper()} ===")
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Umur", "Tanggal Lahir", "JK"]
        for nama, p in pemain.items():
            tabel.add_row([nama, p["umur"], p["tgl"], p["jk"]])
        print(tabel)

def ada_pemain_sama_sekali():
    return any(len(pemain) > 0 for pemain in data_pemain.values())
