from time import sleep


print("""***************
Atm Programı
***************
İşlemler;

1.Para yükleme
2.Para çekme
3.Bakiye sorgulama

Programı sonlandırmak için 'q' ya basınız.
""")

kartiçerdemi = None
bakiye = 1000
kartıyerleştirin = input("Kartı yerleştirmek için 5 rakamını giriniz: ")

if kartıyerleştirin == "5":
    kartiçerdemi = True
    if kartiçerdemi == True:
        while True:
            
            print("\n Bakiye sorgulamak için 1\nPara yüklemek için 2\nPara çekmek için 3\nÇıkmak için 4 rakamını tuşlayınız.")
            işlem = input("İşlem seçiniz: ")
            
            
            if işlem == "1":
                print(f"Toplam bakiyeniz: {bakiye}")
                sleep(3)
                continue
            
            elif işlem == "2":
                parayükle = int(input("Kaç para yüklemek istersiniz: "))
                bakiye = bakiye + parayükle
                print(f"Yeni bakiyeniz: {bakiye}")
                sleep(3)
                continue
            
            elif işlem == "3":
               
                paraçek = int(input("Kaç para çekmek istersiniz"))
                if bakiye - paraçek >= 0:
                    bakiye = bakiye - paraçek
                    print(f"Yeni bakiyeniz{bakiye}")
                    sleep(3)
                    continue
               
                else:
                    print(f"Yetersiz Bakiye...\nMevcut bakiye {bakiye}")
                    sleep(3)
                    continue
            
            elif işlem == "4":
                kartiçerdemi = False
            
            if kartiçerdemi == False:
                break                    
