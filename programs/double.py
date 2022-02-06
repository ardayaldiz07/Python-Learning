from matematik import double

while True:
    number = input("Bir sayı giriniz: ")

    if number == "q":
        break
    else:
        number = int(number)
        print(double(number))
