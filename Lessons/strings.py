arda = str('arda')  # Tek tırnakla string yapabilirsin.
Arda = str("arda")  # Çift tırnakla string yapabilirsin.

a = str('Arda\'nın bugün dersi var')  # \ değil demektir.
print(a)
print(a[0])  # İndeksler 0'dan başlar.
print(a[-1])  # -1 Son karakterdir.

# String parçalama

# 0'ıncı elemandan 3'üncü elemana kadar böler, 3 üncü indeksi almaz.
print(a[0:3])
print(a[:5])  # Baştan başlar 5 e kadar gider.
print(a[3:])  # 3 den başlar sona kadar gider.
print(a[:])  # Tüm stringi alır.
print(a[::2])  # 2 şer 2 şer böler.
print(a[0:8:2])
print(a[::-1])  # Stringi tersten yazar.

b = "PytHon ProGrAmlA DiLi ÇOk KOlay"
print(len(b))
c = "Arda"
d = "Yaldız"
e = "Mükemmel"
print(c +" "+d+" "+e)