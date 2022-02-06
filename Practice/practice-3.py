print("""*****************
Faktöryel Bulma
Çıkmak için q basın
*****************""")

# f = int(input("Hangi sayının faktöryelini bulmak istersiniz?: "))
# print(*range(2,f+1))

while True:
    number = input("Hangi sayını faktöryelini bulmak istersiniz?: ")

    if number == "q":
        print("Program kapatılıyor...")
        break
    else:
        number = int(number)

    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    print(factorial)
