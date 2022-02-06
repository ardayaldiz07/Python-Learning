print("Oyuncu Kaydetme Programı.")


name = str(input("Oyuncunun Adını Giriniz: "))
lastName = str(input("Oyuncunun Soy Adını Giriniz: "))
team = str(input("Oyuncunun Takımını giriniz: "))

info = [name, lastName, team]

print("Oyuncu bilgileri\nOyuncunun Adı: {}\nOyuncunun Soy Adı: {}\nOyuncunun Takımı:{}".format(
    info[0], info[1], info[2]))
