print("Ascii Kodu | Karakter")
print("-----------|---------")

for kod in range(128):  
    #0-127 arasindaki kodlar (sayilar) için
    if  (0 <= kod <= 31) or (kod == 127) :
         karakter = "Kontrol karakteri"  # 0-31 arası ve 127 kontrol karakteri
    elif kod == 32:
        karakter = "[boşluk]"  # 32 boşluk karakteri
    else:  # Diğer karakterler
         karakter = chr(kod)
         
    print(kod, "           |", karakter)