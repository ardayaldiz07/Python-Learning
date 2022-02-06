print("Hello world")
print("{}+{}={}".format(1, 4, 5))
print("Ocak\tŞubat\tMart")
a = "Arda"
b = "Umut"
c = "Hafize"


print(a, b, c, sep=" ")
print(a, b, c, sep="\n")
print(*"Arda", sep="\n")

# stringlerde formatlama

a = int(input("Bir sayı giriniz: "))
b = int(input("Bir sayı giriniz: "))
sum = int(a+b)
print("{} + {} = {}".format(a, b, sum))
print("{:.2f} {:.3f} {:.2f}".format(3.1587, 3.8998, 4.5687))
# Formatlama tiplerini ezberlemene gerek yok https://pyformat.info
