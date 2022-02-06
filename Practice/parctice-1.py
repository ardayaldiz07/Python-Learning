def tambölenleribulma(sayı):
    tam_bölenler = []

    for i in range(2, sayı):

        if (sayı % i == 0):
            tam_bölenler.append(i)

    return tam_bölenler


while True:
    sayı = input("Sayı: ")

    if sayı == "q":
        print("Programdan çıkılıyor...")
        break
    else:
        sayı = int(sayı)
        print(tambölenleribulma(sayı))
