
data_nilai_siswa = [
    {
        'nama': 'Almer Siregar',
        'nis': 'IPA001',
        'kelas': 'IPA',
        'nilai': 85,
        'keterangan': 'Lulus'
    },
    {
        'nama': 'Fariz Albouni',
        'nis': 'IPA002',
        'kelas': 'IPA',
        'nilai': 75,
        'keterangan': 'Lulus'
    },
    {
        'nama': 'Rafa Wiraputera',
        'nis': 'IPS003',
        'kelas': 'IPS',
        'nilai': 90,
        'keterangan': 'Lulus'
    },
    {
        'nama': 'Andika Demitra',
        'nis': 'IPS004',
        'kelas': 'IPS',
        'nilai': 55,
        'keterangan': 'Tidak Lulus'
    },
    {
        'nama': 'Vando Cader',
        'nis': 'IPA005',
        'kelas': 'IPA',
        'nilai': 65,
        'keterangan': 'Tidak Lulus'
    }
]

# Fungsi pause untuk memberikan jeda saat data ditampilkan
def pause():
    input("\nTekan Enter untuk melanjutkan...")

# Fungsi untuk menampilkan data nilai siswa
def tampil_data():
    if not data_nilai_siswa:
        print("Tidak ada data siswa yang tersimpan.")
        pause()
        return

    while True:
        print("\nSub-Menu Tampil Data:")
        print("1. Tampil Data Gabungan")
        print("2. Tampil Data IPA")
        print("3. Tampil Data IPS")
        print("4. Kembali ke Menu Utama")
        
        sub_pilihan = input("\nPilih sub-menu (1-4): ")
        
        data_tampilan = []
        
        if sub_pilihan == '1':
            data_tampilan = data_nilai_siswa
        elif sub_pilihan == '2':
            data_tampilan = [data for data in data_nilai_siswa if data['kelas'] == 'IPA']
        elif sub_pilihan == '3':
            data_tampilan = [data for data in data_nilai_siswa if data['kelas'] == 'IPS']
        elif sub_pilihan == '4':
            break
        else:
            print("\nPilihan tidak valid. Silakan masukkan pilihan yang benar.")
            pause()
            continue
        
       
        if not data_tampilan:
            print("\nTidak ada data untuk kelas yang dipilih.")
        else:
            print("=" * 80)
            print("| {:<20} | {:<10} | {:<6} | {:<5} | {:<15} |".format("Nama", "NIS", "Kelas", "Nilai", "Keterangan"))
            print("=" * 80)
            for data in data_tampilan:
                print("| {:<20} | {:<10} | {:<6} | {:<5} | {:<15} |".format(
                    data['nama'], data['nis'], data['kelas'], data['nilai'], data['keterangan']))
            print("=" * 80)

        pause()

# Fungsi untuk memastikan angka nis adalah uniqe value
def is_nis_unique(nis):
    for data in data_nilai_siswa:
        if data['nis'] == nis:
            return False 
    return True


# Fungsi untuk memastikan sebuah input adalah angka
def get_numeric_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Masukkan angka.")

# Fungsi untuk mengambil bagian nomor dari NIS
def get_number_from_nis(nis):
    return int(nis[3:])  

# Fungsi untuk menambahkan data nilai siswa
def tambah_data():
    print("\nTambah Data Siswa:")
    
    while True:
        nama = input("Nama siswa: ").title()
        if any(char.isdigit() for char in nama):
            print("Nama tidak boleh mengandung angka.")
        else:
            break
    
    while True:
        kelas = input("Kelas siswa (IPA/IPS): ").lower()
        if kelas == "ipa":
            kelas_display = "IPA"
        elif kelas == "ips":
            kelas_display = "IPS"
        else:
            print("Kelas tidak valid. Harap masukkan IPA atau IPS.")
            continue

        if data_nilai_siswa:
            max_nis = max(data_nilai_siswa, key=lambda x: get_number_from_nis(x['nis']))['nis']
            idx = get_number_from_nis(max_nis) + 1
        else:
            idx = 1

        nis = f"{kelas_display}{idx:03}"
        break
    
    while True:
        nilai_input = input("Nilai siswa: ")
        if not nilai_input.isdigit():
            print("Nilai harus berupa angka.")
        else:
            nilai = int(nilai_input)
            if nilai < 0 or nilai > 100:
                print("Nilai harus di antara 0 dan 100.")
            else:
                break
    
    keterangan = 'Lulus' if nilai >= 60 else 'Tidak Lulus'
    
    data_nilai_siswa.append({
        'nama': nama,
        'nis': nis,
        'kelas': kelas_display,
        'nilai': nilai,
        'keterangan': keterangan
    })

    print("Data siswa berhasil ditambahkan!")


# Fungsi untuk menghapus data nilai siswa
def hapus_data():
    tampil_data_gabungan()

    nis = input("Masukkan NIS siswa yang ingin dihapus : ") 
    
    for data in data_nilai_siswa:
        if data['nis'] == nis:
            data_nilai_siswa.remove(data)
            print("Data siswa berhasil dihapus!")
            break
    else:
        print("Data siswa dengan NIS tersebut tidak ditemukan.")



# Fungsi untuk melakukan edit data
def edit_data():
    tampil_data_gabungan()

    nis = input("\nMasukkan NIS siswa yang ingin diedit: ") 
    for data in data_nilai_siswa:
        if data['nis'] == nis:
            print("Data ditemukan!")
            
            data['nama'] = input("Masukkan nama baru (Tekan enter untuk melewati): ").title() or data['nama']
            
            new_kelas = input("Masukkan kelas baru (IPA/IPS) (Tekan enter untuk melewati): ").lower()
            if new_kelas == "ipa" or new_kelas == "ips":
                if data['kelas'].lower() != new_kelas:
                    data['kelas'] = new_kelas.upper()
                    last_num = int(data['nis'][3:])
                    data['nis'] = new_kelas.upper() + str(last_num).zfill(3)
            else:
                print("Kelas tidak valid. Kelas tidak berubah.")
            
            try:
                nilai_baru = input("Masukkan nilai baru (Tekan enter untuk melewati): ")
                if nilai_baru:
                    nilai_baru = int(nilai_baru)
                    if 0 <= nilai_baru <= 100:
                        data['nilai'] = nilai_baru
                        data['keterangan'] = 'Lulus' if data['nilai'] >= 60 else 'Tidak Lulus'
                    else:
                        print("Nilai harus di antara 0 dan 100.")
                else:
                    print("Nilai tidak berubah.")
            except ValueError:
                print("Masukkan nilai yang valid!")
            
            print("Data siswa berhasil diperbarui!")
            return
    print("Data siswa dengan NIS tersebut tidak ditemukan.")

#Fungsi untuk menampilkan data gabungan
def tampil_data_gabungan(): 
    if not data_nilai_siswa:
        print("\nTidak ada data siswa yang tersimpan.")
        return
    
    print("=" * 80)
    print("| {:<20} | {:<10} | {:<6} | {:<5} | {:<15} |".format("Nama", "NIS", "Kelas", "Nilai", "Keterangan"))
    print("=" * 80)
    for data in data_nilai_siswa:
        print("| {:<20} | {:<10} | {:<6} | {:<5} | {:<15} |".format(
            data['nama'], data['nis'], data['kelas'], data['nilai'], data['keterangan']))
    print("=" * 80)



# Fungsi untuk menampilkan rata - rata nilai siswa
def rata_rata_nilai():
    total_nilai = sum([data['nilai'] for data in data_nilai_siswa])
    avg = total_nilai / len(data_nilai_siswa) if data_nilai_siswa else 0
    print(f"Rata-rata nilai siswa gabungan adalah: {avg:.2f}")
    
    while True:
        print("\nSub-Menu Rata-Rata Nilai:")
        print("1. Tampil Rata-Rata IPS")
        print("2. Tampil Rata-Rata IPA")
        print("3. Kembali")
        
        sub_pilihan = int(input("Pilih sub-menu (1-3): "))
        
        if sub_pilihan == 1:
            tampil_rata_rata_ips()
        elif sub_pilihan == 2:
            tampil_rata_rata_ipa()
        elif sub_pilihan == 3:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

# Fungsi untuk rata - rata nilai IPS
def tampil_rata_rata_ips():
    total_nilai_ips = sum([data['nilai'] for data in data_nilai_siswa if data['kelas'] == "IPS"])
    count_ips = len([data for data in data_nilai_siswa if data['kelas'] == "IPS"])
    avg_ips = total_nilai_ips / count_ips if count_ips else 0
    print(f"Rata-rata nilai IPS siswa adalah: {avg_ips:.2f}")

# Fungsi untuk rata - rata nilai IPA
def tampil_rata_rata_ipa():
    total_nilai_ipa = sum([data['nilai'] for data in data_nilai_siswa if data['kelas'] == "IPA"])
    count_ipa = len([data for data in data_nilai_siswa if data['kelas'] == "IPA"])
    avg_ipa = total_nilai_ipa / count_ipa if count_ipa else 0
    print(f"Rata-rata nilai IPA siswa adalah: {avg_ipa:.2f}")

# Fungsi untuk menampilkan menu
def menu():
    print("="*36)
    print("    Aplikasi Data Nilai Siswa SMA    ")
    print("          Kelas 12 IPA & IPS        ")
    print("="*36)
    while True:
        print("\nMenu:")
        print("1. Tampilkan Daftar Nilai Siswa")
        print("2. Menambah Data Siswa Baru")
        print("3. Menghapus Data Siswa")
        print("4. Edit Data Siswa")
        print("5. Rata-rata Nilai Siswa")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if pilihan == '1':
            tampil_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            hapus_data()
        elif pilihan == '4':
            edit_data()
        elif pilihan == '5':
            rata_rata_nilai()
        elif pilihan == '6':
            print("\nTerima kasih, Bapak/Ibu Guru, telah menggunakan aplikasi Data Nilai Siswa SMA.")
            print("Sampai jumpa kembali!")

            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

print("Selamat datang, Bapak/Ibu Guru yang terhormat.")
print("Silakan pilih menu yang tersedia untuk memulai.")
menu()
