import sys

def kira():
    bmi = berat/tinggi**2
    if bmi<18.5:
        kategori='kurang berat badan'
    elif 18.5<=bmi<25:
        kategori='berat yang sihat'
    elif 25<=bmi<=30:
        kategori='lebih berat badan'
    else:
        kategori='gemuk'
    return (bmi, kategori)

def input_pengguna ():
    nama = input ("masukkan nama anda dawg:")
    berat = float(input("masukkan berat badan anda wahai fine shyt:"))
    tinggi = float (input("masukkan tinggi anda dalam meter:"))
    return (nama, berat, tinggi)

while True:
    answer = input("masukkan pengiraan BMI fineshyt [Y/N] >>>")
    if answer in ["Y" , "y"]:
        nama, berat, tinggi = input_pengguna()
        bmi, kategori= kira()
        print("****profile bmi fine shyt****")
        print("Nama :", nama)
        print("berat:", berat, "Kg")
        print("tinggi:", tinggi, "m")
        print("index bmi anda ialah", round (bmi , 2))
        print("kategori fine shyt adalah", kategori)

    else:
        print ("thankyou fineshyt dawg")
        sys.exit()
    
