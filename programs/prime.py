from time import sleep


def asal_mi(sayı):
    if (sayı == 1):
        return False

    elif(sayı == 2):
        return True
    else:
        for i in range(2, sayı):
            if (sayı % i == 0):
                return False
        return True


while True:
    sayı = input("Sayı: ")

    if sayı == "q":
        print("Programdan çıkılıyor...")
        break
    else:
        if (asal_mi(sayı == True)):
            print("Sayı asal bir sayıdır...")
        else:
            print("Sayı asal değildir...")
        sleep(1)
