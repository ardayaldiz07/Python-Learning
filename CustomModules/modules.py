from mathmodule import factorial
from mathmodule import sum


while True:

    operator = input("İşlem seçiniz: ")

    if operator == "q":
        break
    elif operator == "faktöryel":
        number1 = int(input("Bir sayı giriniz: "))
        print(factorial(number1))
    elif operator == "toplama":
        number1 = int(input("Bir sayı giriniz: "))
        number2 = int(input("Bir sayı giriniz: "))

        print(sum(number1,number2))
            