todo_list = []

# nampilin menu
def tampilkan_menu():
    print("\n===== TO DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Tandai Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

# nambah tugas
def tambah_tugas():
    tugas = input("Masukkan tugas: ")

    if tugas == "":
        print("Tugas tidak boleh kosong!")
    else:
        data = {
            "nama": tugas,
            "selesai": False
        }

        todo_list.append(data)
        print("Tugas berhasil ditambahkan!")

# liat tugas
def lihat_tugas():
    if len(todo_list) == 0:
        print("Belum ada tugas.")
    else:
        print("\n===== DAFTAR TUGAS =====")

        nomor = 1

        for tugas in todo_list:
            status = "Belum"

            if tugas["selesai"]:
                status = "Selesai"

            print(f"{nomor}. {tugas['nama']} [{status}]")
            nomor += 1

# tanda selesai
def tandai_selesai():
    lihat_tugas()

    if len(todo_list) > 0:
        nomor = int(input("Pilih nomor tugas: "))

        if nomor >= 1 and nomor <= len(todo_list):
            todo_list[nomor - 1]["selesai"] = True
            print("Tugas sudah diselesaikan!")
        else:
            print("Nomor tidak valid!")

# mengapus tugas
def hapus_tugas():
    lihat_tugas()

    if len(todo_list) > 0:
        nomor = int(input("Pilih nomor tugas yang ingin dihapus: "))

        if nomor >= 1 and nomor <= len(todo_list):
            todo_list.pop(nomor - 1)
            print("Tugas berhasil dihapus!")
        else:
            print("Nomor tidak valid!")

# program utamanya
while True:
    tampilkan_menu()

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        tandai_selesai()

    elif pilihan == "4":
        hapus_tugas()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Menu tidak tersedia!")