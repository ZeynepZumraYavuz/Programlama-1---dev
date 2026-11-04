print("Döngülü Hesap Makinesi")

while True: # Programın sonsuz döngüye girmesini sağalar. İşlem bittiğinde menü tekrar ekrana gelir.
    print("--------------------")
    print("+ Toplam (+)")
    print("- Çıkarma (-)")
    print("* Çarpma (*)")
    print("* Üs Alma (*)")
    print("// Tam Bölme (//)")
    print("q Çıkış") # Kullanıcı prgoramdan istediği zaman çıkabilmesi için quit.
    print("--------------------")
    
    # Kullanıcıdan işlem seçimi alıyoruz.
    
    secim = input("Yapmak istediğiniz işlemi girin (+,-,*,/,// veya çıkış için 'q'): ")
    
    # Çıkış koşulu
    
    if secim.lower() == 'q':
    
        print("Hesap makinesinden çıkılıyor")
    break # Döngüyü kır.
    # Geçerli bir işlem seçilip seçilmediğini kontrol ediyoruz.
    
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    # Kullanıcıdan sayıyı alıyoruz.
    
    print("--------------------")
    
    #Toplama
    if secim == '+':
        sonuc = sayi1 + sayi2
        print(f"Sonuç:{sayi1} + {sayi2} = {sonuc}")
        
    #Çıkarma
    elif secim == '-': #if değilse elif.
        sonuc = sayi1 - sayi2 
        print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
 
    #Çarpma
    elif secim == '*':
        sonuc = sayi1 * sayi2
        print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
    
    #Bölme
    elif secim == '/':
        if sayi2 != 0: # sayi2 0 değilse işlemi yap.
            sonuc = sayi1 / sayi2
            print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
        else:
            print("Hata: Bir sayı 0'a bölünemez!")
    
#sayi2 0 ise.

    #Üs Alma
    elif secim == '**':
            sonuc = sayi1 ** sayi2
            print(f"Sonuç:{sayi1} ** {sayi2} = {sonuc}")
    
    #Tam Bölme
    elif secim == '//':
        if sayi2 != 0:
                sonuc = sayi1 // sayi2
                print(f"Sonuç: {int(sayi1)} // {int(sayi2)} = {int(sonuc)}")
        else:
                print("Hata: Bir sayı 0'a bölünemez!")