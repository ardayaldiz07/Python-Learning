boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki =  kilo / (boy ** 2)

if (bki < 18.5):
    print("Zayıf")
elif (bki >= 18.5 and bki < 25):
    print("Normal")
elif (bki >= 25 and bki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")