#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

#Hipotenüs Formülü: a^2 + b^2 = c^2

side1 = int(input("Sayı girin: "))
side2 = int(input("Sayı girin: "))
c = (side1 **2 + side2**2) ** 0.5
print("hipotenüs:",c)