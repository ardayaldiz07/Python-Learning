# cinsiyet = input("Cinsiyetinizi seçin: ")
# isim = input("İsminizi Girin: ")

def Selamla(cinsiyet, isim):

    if cinsiyet == "1":
        cinsiyet = "bey"
    elif cinsiyet == "2":
        cinsiyet = "hanım"
    print("Merhaba {} {} nasılsınız ?".format(isim, cinsiyet))


Selamla(isim=input("isminizi Giriniz"),
        cinsiyet=input("Cinsiyetinizi giriniz"))
        
