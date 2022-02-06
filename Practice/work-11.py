number = int(input("Bir sayı giriniz: "))

i = 1
total = 0

while (i<number):
    if (number % i == 0):
        total += i 
    i += 1
if total == number:
    print("Sayı mükemmel sayıdır.")
else:
    print("Sayı mükemmel sayı değildir.")            