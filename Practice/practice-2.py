a = int(input("Bir sayı giriniz: "))
b = int(input("Bir sayı giriniz: "))
c = int(input("Bir sayı giriniz: "))

delta = b**2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print(f"Birinci Kök:{x1}\nİkinci Kök:{x2}") #Kendi Yöntemim
print("Birinci Kök: {}\nİkinci Kök: {}".format(x1,x2)) #Söylenilen Yöntem 
