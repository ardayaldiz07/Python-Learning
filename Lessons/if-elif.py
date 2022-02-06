a = input("İşlem seçiniz: ")
if a == "1":
    print("İşlem 1 seçildi.")
elif a == "2":
    print("İşlem 2 seçildi.")
elif a == "3":
    print("İşlem 3 seçildi.")
else:
    print("Geçersiz işlem")    

note = float(input("Notunuzu girin: "))
if note >= 90:
    print("Notunuz A+") 
elif note >= 80:
    print("Notunuz A")
elif note >= 70:
    print("Notunuz B")