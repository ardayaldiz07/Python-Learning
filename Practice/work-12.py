sayı = input("Sayı Giriniz: ")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
    