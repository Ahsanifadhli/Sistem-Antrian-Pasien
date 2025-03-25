from collections import deque

antrian_pasien = deque()

def Dashboard():
    if antrian_pasien:
        print("\n☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
        print("          📋 Data Antrian Pasien Puskesmas 📋          ")
        print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
        for index, (nama, esi) in enumerate(antrian_pasien, start=1):
            print(" No. Antrian  : " , index)
            print(" Nama Pasien  : " , nama)
            print(" Level ESI    : " , esi)
            print("-------------------------------------------------------")
    else:
        print("\n⚠️ Tidak ada data pasien dalam antrian.\n")

def TambahAntrian():
    while True:
        NamaPasienNormal = input("Masukkan Nama Pasien (Non Darurat): ")
        # Menambahkan pasien non-darurat dengan level ESI 5
        antrian_pasien.append((NamaPasienNormal, 5))
        print("Berhasil, saudara/i", NamaPasienNormal, " telah ditambahkan ke antrian.")
        
        while True:  # Loop untuk validasi input
            PeriksaPasienNormal = input("Apakah ada pasien lagi? (Y/N): ").upper()
            
            if PeriksaPasienNormal == "Y":  # Jika input "Y" atau "y"
                break  # Keluar dari loop validasi, melanjutkan loop utama
                
            elif PeriksaPasienNormal == "N":  # Jika input "N" atau "n"
                print("Baik, terima kasih atas konfirmasinya.")
                return  # Mengakhiri fungsi, keluar dari kedua loop
                
            else:  # Jika input tidak valid
                print("⚠️ Error. Mohon masukkan Y (ya) atau N (tidak).")

def TambahAntrianDarurat():
    while True:
        NamaPasienDarurat = input("Masukkan Nama Pasien Darurat: ")
        while True:
            print("\nLevel ESI (Emergency Severity Index):")
            print("1. ESI 1 (Kondisi Kritis)")
            print("2. ESI 2 (Kondisi Gawat)")
            print("3. ESI 3 (Kondisi Sedang)")
            print("4. ESI 4 (Kondisi Tidak Mendesak)")
            print("5. ESI 5 (Kondisi Tidak Mendesak)")
            LevelDarurat = int(input("Masukkan Level ESI Pasien (1-5): "))
            if LevelDarurat in [1, 2, 3, 4, 5]:
                # Menempatkan pasien darurat ke depan berdasarkan prioritas ESI
                if LevelDarurat == 1:
                    antrian_pasien.appendleft((NamaPasienDarurat, LevelDarurat))
                elif LevelDarurat == 2:
                    antrian_pasien.insert(1, (NamaPasienDarurat, LevelDarurat))
                elif LevelDarurat == 3:
                    antrian_pasien.insert(2, (NamaPasienDarurat, LevelDarurat))
                else:
                    antrian_pasien.append((NamaPasienDarurat, LevelDarurat))  # ESI 4-5 di belakang
                print("Berhasil, saudara/i", NamaPasienDarurat, " dengan level ESI", LevelDarurat, " telah ditambahkan ke antrian.\n")
                break
            else:
                print("⚠️ Error, coba masukkan lagi.")

        while True:  # Loop untuk validasi input
            PeriksaPasienDarurat = input("Apakah ada pasien lagi? (Y/N): ").upper()
            
            if PeriksaPasienDarurat == "Y":  # Jika input "Y" atau "y"
                break  # Keluar dari loop validasi, melanjutkan loop utama
                
            elif PeriksaPasienDarurat == "N":  # Jika input "N" atau "n"
                print("Baik, terima kasih atas konfirmasinya.")
                return  # Mengakhiri fungsi, keluar dari kedua loop
                
            else:  # Jika input tidak valid
                print("⚠️ Error. Mohon masukkan Y (ya) atau N (tidak).")
            
def UpdateAntrian():
    while True:
        print("1. Tambah Antrian")
        print("2. Tambah Antrian (Darurat)")
        x = int(input("Pilih Menu: "))
        if x == 1:
            TambahAntrian()
            break
        elif x == 2:
            TambahAntrianDarurat()
            break
        else:
            print("⚠️ Error, coba masukkan lagi.")

def SesiPemanggilanAntrian():
    if antrian_pasien:
        pasien, esi = antrian_pasien.popleft()
        print("◈◇◈ Pasien atas nama", pasien, " dengan level ESI", esi, " sedang dalam proses pelayanan.◇◈◇")
    else:
        print("Tidak ada pasien dalam antrian.")

def LihatJumlahAntrianPasien():
    print("\n💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
    print("💠       Jumlah pasien dalam antrian saat ini: " , len(antrian_pasien) , " orang.   💠")
    print("💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠💠")
        
while True:
    print("\n=============================================")
    print("       ❁❀❃ Sistem Antrian Pasien ❃❁❀")
    print("  Selamat Datang di Sistem Antrian Rumah Sakit Delima")
    print("=============================================")
    print("1. Dashboard antrian")
    print("2. Update Antrian")
    print("3. Sesi Pemanggilan Antrian")
    print("4. Jumlah Antrian Pasien")
    print("5. Keluar")
    x = int(input("Pilih Menu: "))
    if x == 1:
        Dashboard()
    elif x == 2:
        UpdateAntrian()
    elif x == 3:
        SesiPemanggilanAntrian()
    elif x == 4:
        LihatJumlahAntrianPasien()
    elif x == 5:
        print("☘☘☘ Terimakasih | Thank You | ありがとうございます ☘☘☘")
        break
    else:
        print("Error, coba masukkan lagi.")
