sayi1 = int(input("Deger Giriniz : "))
sayi2 = int(input("Deger Giriniz : "))
islem = input("İslemi Giriniz : (+, -, *, /, //, **):")


if sayi1 > sayi2:
    print("sayi1 büyükmüs ")

if sayi2 > sayi1:
    print("sayi2 büyükmüş")
    
if sayi1 == sayi2:
    print("sayılar eşitmiş")

deger = input("Devam etmek için ('e') : ")

if deger.lower() == "e":
    print("girilen deger e imiş")

if islem == "+":
    print("Toplama İşleminin Sonucu : ", (sayi1 + sayi2))
elif islem == "-":
    print("Çıkarma İşleminin Sonucu : ", (sayi1 - sayi2))
elif islem == "*":
    print("Çarpma İşleminin Sonucu : ", (sayi1 * sayi2))
elif islem == "/":
    if sayi2 == 0:
        print("Sıfıra Bölünme Hatası.")
    else:
        print("Bölme İşleminin Sonucu : ", (sayi1 / sayi2))
elif islem == "//":
    if sayi2 == 0:
        print("Sıfıra Bölünme Hatası.")
    else:
        print("TamBölme İşleminin Sonucu : ", (sayi1 // sayi2))
elif islem == "**":
    print("ÜsAlma İşleminin Sonucu : ", (sayi1 ** sayi2))
else:
    print("Geçersiz işlem girdiniz!")