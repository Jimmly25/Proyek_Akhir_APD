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

def lihat_pemain_berdasarkan_tim():
    tim = input("Masukkan nama TIM: ").strip()

    if tim not in data_pemain:
        print(f"❌ Tim '{tim}' tidak ditemukan.\n") 
        return

    print(f"\n=== TIM {tim.upper()} ===")
    tabel = PrettyTable()
    tabel.field_names = ["Nama", "Umur", "Tanggal Lahir", "Game", "Jenis Kelamin"]

    for nama, p in data_pemain[tim].items():
        tabel.add_row([nama, p["umur"], p["tgl"], p["game"], p["jk"]])

    print(tabel)
    print()


def lihat_semua_pemain():
    if not data_pemain:
        print("\n❗ Belum ada pemain.\n")
        return

    for tim, pemain in data_pemain.items():
        print(f"\n=== TIM {tim.upper()} ===")
        tabel = PrettyTable()
        tabel.field_names = ["Nama", "Umur", "Tanggal Lahir", "Game", "Jenis Kelamin"]

        for nama, p in pemain.items():
            tabel.add_row([nama, p["umur"], p["tgl"], p["game"], p["jk"]])

        print(tabel)


def ubah_pemain():
    tim = input("Masukkan TIM pemain: ").strip()
    if tim not in data_pemain:
        print(f"❌ Tim '{tim}' tidak ditemukan.\n")
        return

    nama = input("Masukkan nama pemain: ").strip()
    if nama not in data_pemain[tim]:
        print("❌ Nama pemain tidak ditemukan!\n")
        return

    data = data_pemain[tim][nama]


    new_nama = input("Nama baru (Enter lewati): ").strip() or nama

    new_umur_in = input("Umur baru (Enter lewati): ").strip()
    new_umur = None
    if new_umur_in:
        try:
            umur_val = int(new_umur_in)
            if umur_val > 0:
                new_umur = umur_val
            else:
                print("❌ Umur harus lebih dari 0! Tidak diubah.")
        except:
            print("❌ Umur harus angka! Tidak diubah.")

    new_tgl = input("Tanggal lahir baru (dd-mm-yyyy / Enter lewati): ").strip()
    if new_tgl:
        try:
            d, m, y = map(int, new_tgl.split("-"))
        except:
            print("❌ Format tanggal salah! Tidak diubah.")
            new_tgl = None

    new_tim = input("Pindah ke TIM lain? (nama TIM / Enter): ").strip() or tim
    new_game = input("Game baru (Enter lewati): ").strip()

    # Perbaikan jenis kelamin: seperti tanggal lahir, salah input tidak diubah
    new_jk = input("Jenis kelamin baru (L/P/Enter): ").upper().strip()
    if new_jk not in ("L", "P"):
        print("❌ Input salah! Jenis kelamin tidak diubah.")
        new_jk = None


    if new_nama != nama:
        data_pemain[tim][new_nama] = data_pemain[tim].pop(nama)
        nama = new_nama

    if new_umur is not None:
        data["umur"] = new_umur
    if new_tgl:
        data["tgl"] = new_tgl
    if new_game:
        data["game"] = new_game
    if new_jk:
        data["jk"] = new_jk

    if new_tim != tim:
        if new_tim not in data_pemain:
            data_pemain[new_tim] = {}
        data_pemain[new_tim][nama] = data_pemain[tim].pop(nama)
        if not data_pemain[tim]:
            del data_pemain[tim]
            print(f"ℹ Tim '{tim}' otomatis dihapus.")

    print("✅ Data pemain berhasil diperbarui!\n")



def hapus_pemain():
    tim = input("Masukkan TIM pemain: ").strip()

    if tim not in data_pemain:
        print(f"❌ Tim '{tim}' tidak ditemukan.\n")
        return

    nama = input("Masukkan nama pemain: ").strip()

    try:
        del data_pemain[tim][nama]
        print(f"✅ Pemain '{nama}' berhasil dihapus.\n")
    except KeyError:
        print("❌ Nama pemain tidak ditemukan!\n")
        return

    if not data_pemain[tim]:
        del data_pemain[tim]
        print(f"ℹ Tim '{tim}' otomatis dihapus karena kosong.\n")
