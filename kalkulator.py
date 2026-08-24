from termcolor import colored
from fractions import Fraction 
import time 

# PENYAMBUTAN KEPADA USER 
print(colored("==========selamat datang di kalkulator sederhana==========", "white"))
time.sleep(1)

# input pembayaran kepada user
print(colored("masukkan jumlah pembayaran kalau mau make kalkulator (transfer ke dana nomor 081264058352)", "light_green"))
time.sleep(1) 
while True:
    sudah_bayar = str(input(colored("apakah sudah dibayar? (ya/tidak): ", "light_magenta")))
    if sudah_bayar == "ya":
        print(colored("lanjutkan temankuhhhhh 😎😎😎", "white"))
        break
    elif sudah_bayar == "tidak":
        print(colored("wet, gak boleh make, bayar dulu 🤑🤑🤑", "white"))
        continue
        sudah_bayar
    else:
        print(colored("ngetik apaan sih? 😒😒😒", "white"))
        continue
        sudah_bayar
    
while True:
    pembayaran = int(input("masukkan nominal uang yang telah dibayar : ")) 
    if pembayaran < 100000:
        print("awokawok langganan kalkulator aja gak bisa, pembayaran lu tidak mencukupi. bayar ulang!! 🤣🤣🤣")
        continue
        pembayaran
    elif pembayaran == 100000:
        print("pembayaran diterima, selamat menggunakan kalkulator 😇😇😇")
        break
    elif pembayaran > 100000:
        print("makasih bang lebihnya semoga sehat2 terus dan lancar rezekinya 😻😻😻")
        break
    else:
        print("ngetik apaan sih?")
        continue
        pembayaran

# input kata sandi 
kata_sandi = ["adek ganteng" or "mobile legends" or "sandinya adalah"]
input_sandi = str(input("masukkan kata sandi untuk mengakses kalkulator: "))
if input_sandi == ("adek ganteng") :
    print("akses diterima 😁😁😁")
elif input_sandi == ("mobile legends") :
    print("akses diterima 😁😁😁")
elif input_sandi == ("sandinya adalah") :
    print("akses diterima 😁😁😁")
else:
    print("wkwkwkwk, liat di pembayaran, akses ditolak 😂😂😂") 
    exit()

# input mode kalkulator 
mode = str(input("pilih mode kalkulator (dasar, pecahan, persen, pangkat, akar kuadrat); "))

# input angka & operator perhitungan
if mode == "pecahan":
    angka_1 = float(Fraction(input("masukkan pembilang pertama : ")))
    angka_2 = float(Fraction(input("masukkan penyebut pertama : ")))
    angka_3 = float(Fraction(input("masukkan pembilang kedua : ")))
    angka_4 = float(Fraction(input("masukkan penyebut kedua : ")))
    pilih_operator_pecahan = str(input("pilih operator (+, -, *, /): "))
    #lanjutan dari sistem pecahan
    angka_11 = int(angka_1)
    angka_22 = int(angka_2)
    angka_33 = int(angka_3)
    angka_44 = int(angka_4)
elif mode == "dasar":
    angka_1_1 = float(input("masukkan angka pertama : "))
    angka_2_2 = float(input("masukkan angka kedua : "))
    pilih_operator_dasar = str(input("pilih operator (+, -, *, /): "))
elif mode == "persen":
    persen = float(input("masukkan angka : "))
elif mode == "pangkat":
    angka = float(input("masukkan angka : "))
    pangkat = float(input("masukkan angka pangkat : "))
elif mode == "akar kuadrat":
    angka = float(input("masukkan angka : "))
    akar = int(input("masukkan akar : "))
    akar_kuadrat = 1 / akar
else:
    print("ingat hanya ada 5 opsi!!! 😒😒😒")
    exit() 

if mode == "pecahan":  # mode pecahan
    if pilih_operator_pecahan == "+":
        if angka_22 == 0 or angka_44 == 0:
            print("error, nol gak bisa jadi penyebut")
        else:
            hasil = ((Fraction(angka_11, angka_22)) + (Fraction(angka_33, angka_44)))
            print("hasilnya adalah:", hasil)
        time.sleep(1)
    elif pilih_operator_pecahan == "-":
        if angka_22 == 0 or angka_44 == 0:
            print("error, nol gak bisa jadi penyebut")
        else:
            hasil = ((Fraction(angka_11, angka_22)) - (Fraction (angka_33, angka_44)))
            print("hasilnya adalah:", hasil)
        time.sleep(1)
    elif pilih_operator_pecahan == "*":
        if angka_22 == 0 or angka_44 == 0:
            print("error, nol gak bisa jadi penyebut")
        else:
            hasil = (Fraction(angka_11, angka_22) * Fraction(angka_33, angka_44))
            print("hasilnya adalah:", hasil)
        time.sleep(1)
    elif pilih_operator_pecahan == "/":
        if angka_22 == 0 or angka_44 == 0:
            print("error, nol gak bisa jadi penyebut")
        else:
            hasil = Fraction(angka_11, angka_22) / Fraction(angka_33, angka_44)
            print("hasnya adalah:", hasil)
        time.sleep(1)
    print("angka-angka yang diinput diubah ke integer apabila angka-angka yang diinput berupa float")
    time.sleep(1)

elif mode == "dasar":  #mode dasar 
    if pilih_operator_dasar == "+":
        hasil = angka_1_1 + angka_2_2
        if hasil.is_integer():
            hasil = int(hasil)
            print("hasil penjumlahan:", hasil)
        else:
            print("hasil penjumlahan:", hasil)
        time.sleep(1)
    elif pilih_operator_dasar == "-":
        hasil = angka_1_1 - angka_2_2
        if hasil.is_integer():
            hasil = int(hasil)
            print("hasil pengurangan:", hasil)
        else:
            print("hasil pengurangan:", hasil)
        time.sleep(1)
    elif pilih_operator_dasar == "*":
        hasil = angka_1_1 * angka_2_2
        if hasil.is_integer():
            hasil = int(hasil)
            print("hasil perkalian :", hasil)
        else:
            print("hasil perkalian :", hasil)
        time.sleep(1)
    elif pilih_operator_dasar == "/":
        if angka_2_2 == 0:
            print("error: pembagian dengan nol tidak diperbolehkan")
        else:
            hasil = angka_1_1 / angka_2_2
            if hasil.is_integer():
                hasil = int(hasil)
                print("hasil pembagian:", hasil)
            else:
                print("hasil pembagian:", hasil)
        time.sleep(1)

elif mode == "persen":  # mode persen 
    hasil = persen / 100
    print(hasil, end = " ")
    print("atau", persen, "%")
    time.sleep(1)

elif mode == "pangkat":  # mode pangkat
    hasil = angka ** pangkat
    if hasil.is_integer():
        print("hasilnya adalah : ", int(hasil))
    else:
        print("hasilnya adalah : ", round(float(hasil), 2)) 
    time.sleep(1)

elif mode == "akar kuadrat":
    hasil = angka ** akar_kuadrat
    print("hasilnya adalah : ", round(hasil, 2))
    time.sleep(1) 

print("terimakasih telah menggunakan kalkulator saya 🥳🥳🥳")
time.sleep(1)
print("jangan lupa kasih bintang 5 ya! 🌟🌟🌟🌟🌟")
