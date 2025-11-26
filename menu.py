def header(judul):
    print("\n" + "=" * 60)
    print(judul.center(60))
    print("=" * 60)


def tampilkan_menu_awal():
    header("⚡ SISTEM LOGIN ESPORT ⚡")
    print("""
 [1] 🔐 Login
 [2] 📝 Register
 [3] 🚪 Keluar
""")


def tampilkan_menu_admin():
    header("👑 MENU ADMIN – E-SPORT MANAGER")
    print("""
 [1] ➕ Tambah Pemain
 [2] 📋 Lihat Semua Pemain (Per TIM)
 [3] 🔍 Cari Pemain
 [4] 🏆 Lihat Pemain Berdasarkan TIM      
 [5] ✏️ Ubah Pemain
 [6] ❌ Hapus Pemain
 [7] 🔙 Logout
""")


def tampilkan_menu_user():
    header("🎮 MENU USER – VIEW MODE")
    print("""
 [1] 📋 Lihat Semua Pemain
 [2] 🔍 Cari Pemain
 [3] 🏆 Lihat Pemain Berdasarkan TIM
 [4] 🔙 Logout
""")
