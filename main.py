from auth import login, register, akun
from menu import (
    tampilkan_menu_awal,
    tampilkan_menu_admin,
    tampilkan_menu_user
)
from pemain import (
    tambah_pemain,
    lihat_semua_pemain,
    lihat_pemain_berdasarkan_tim,
    cari_pemain,
    ubah_pemain,
    hapus_pemain
)

program_jalan = True

while program_jalan:
    tampilkan_menu_awal()
    pilih_awal = input("Pilih menu: ").strip()

    # ================== LOGIN ==================
    if pilih_awal == "1":
        user = input("Username: ").strip()
        pw = input("Password: ").strip()

        role = login(user, pw)

        # ================ ADMIN =================
        if role == "admin":
            print("\n✅ Login sebagai ADMIN!\n")

            while True:
                tampilkan_menu_admin()
                pilih = input("Pilih menu: ").strip()

                if pilih == "1":
                    tambah_pemain()
                elif pilih == "2":
                    lihat_semua_pemain()
                elif pilih == "3":
                    cari_pemain()
                elif pilih == "4":
                    lihat_pemain_berdasarkan_tim()
                elif pilih == "5":
                    ubah_pemain()
                elif pilih == "6":
                    hapus_pemain()
                elif pilih == "7":
                    print("🔒 Logout...\n")
                    break
                else:
                    print("❌ Menu tidak valid!\n")

        # ================= USER ==================
        elif role == "user":
            print("\n✅ Login sebagai USER!\n")

            while True:
                tampilkan_menu_user()
                pilih = input("Pilih menu: ").strip()

                if pilih == "1":
                    lihat_semua_pemain()
                elif pilih == "2":
                    cari_pemain()
                elif pilih == "3":
                    lihat_pemain_berdasarkan_tim()
                elif pilih == "4":
                    print("🔒 Logout...\n")
                    break
                else:
                    print("❌ Menu tidak valid!\n")

        else:
            print("❌ Username atau Password salah!\n")

    # ================== REGISTER ==================
    elif pilih_awal == "2":

        # === VALIDASI USERNAME ===
        while True:
            username = input("Buat username: ").strip()
            if not username:
                print("❌ Username tidak boleh kosong!")
                continue
            if username in akun:
                print("❌ Username sudah dipakai!")
                continue
            break

        # === VALIDASI PASSWORD ===
        while True:
            pw = input("Buat password: ").strip()
            if not pw:
                print("❌ Password tidak boleh kosong!")
                continue
            break

        # === VALIDASI ROLE ===
        while True:
            role = input("Daftar sebagai (admin/user): ").strip().lower()
            if not role:
                print("❌ Role tidak boleh kosong!")
                continue
            if role not in ("admin", "user"):
                print("❌ Role harus 'admin' atau 'user'!")
                continue
            break

        register(username, pw, role)

    # ================== KELUAR ==================
    elif pilih_awal == "3":
        print("👋 Terima kasih telah menggunakan sistem ini!")
        program_jalan = False

    else:
        print("❌ Menu tidak valid!\n")
