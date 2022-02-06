# Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

# Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

height = float(input("Boyunuzu girin: "))
weight = int(input("Kilonuzu girin: "))
ind = weight/(height**2)
print(ind)