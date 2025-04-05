import random 

hedef_sayi = random.randint(1,100)
tahmin_sayisi = 0

while True:
    tahmin = int(input("lütfen 1-100 arasında bir sayı gir göt:" ))
    tahmin_sayisi += 1
    
    if tahmin_sayisi > 8:
        print("Tahmin sayınız 8'i geçti. Oyunu kaybettiniz.")
        break   
    if tahmin < hedef_sayi:
        print("daha büyük bir sayı gir salak")
    elif tahmin > hedef_sayi:
        print("daha küçük gir yarrak kafası")
    else:
        print(f"aferin sik kafa {tahmin_sayisi} denemede buldun")
        break

print("oyun bitti tekrar deneyin")