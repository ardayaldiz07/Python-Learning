# For döngüsü.
liste = [1, 2, 3, 4, 5, 6, 7]

for eleman in liste:
    print(eleman)

toplam = 0

for eleman in liste:
    toplam = toplam + eleman
    print("Toplam: {} Eleman: {}".format(toplam, eleman))
print(toplam)


liste2 = [1, 2, 3, 4, 26, 74, 43, 256, 71, 83, 36, 37, 85]
liste3 = ["Çift sayılar"]

for eleman in liste2:
    if eleman % 2 == 0:
        liste3.append(eleman)
print(liste3)

# Stringler üzerinde gezinme
s = "Python"
for i in s:
    print(i*3)

# Demetler üzerinde gezinme

demet = ((1, 2), (3, 4), (5, 6), (7, 8))

for (i, j) in demet:
    print(f"İ: {i} J: {j}")


demet2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

for (a, b, c) in demet2:
    print(f"A: {a} B: {b} C: {c}")


# Sözlük üzerinde gezinme.

sözlük = {"bir": 1, "iki": 2, "üç": 3}

for eleman in sözlük:
    print(eleman)

for eleman in sözlük.values():
    print(eleman)

for (i, j) in sözlük.items():
    print(f"Anahtar: {i} Değer: {j}")
