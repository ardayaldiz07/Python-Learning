from time import sleep

total = 0
while True:
    number = input("Bir sayı girin: ")
    if number == "q":
        print("Programdan Çıkılıyor...\n","Toplam = ",total)
        sleep(1)
        break
    else:
        number = int(number)
        total += number
        sleep(0.3)

