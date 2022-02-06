# Değişkenler = Herhangi bir veri tipinden değer tutar.
# String = Karakter değeri alır.

Arda = str("Arda")
a = str("Yaldız")
print(Arda+" "+a)
Arda = 5
print(Arda)

Arda, a = a, Arda
# Arda ve a değişkeninin değerlerini birbiriyle değiştirdim.
print(a)
print(Arda)

a += 1
print(a)
