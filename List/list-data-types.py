liste1 = ["Elma", 35, "Merhaba", 3.14, 5]
liste2 = list()  # Boş liste oluşturma.
print(len(liste1))
print(liste1[2])
print(liste1[-1])
print(liste1[:4])
print(liste1[0:4:2])
# Temel liste metodları
liste3 = [1, 2, 3]
liste4 = [4, 5, 6]
liste5 = liste3+liste4
print(liste5)
liste3[0] = 4
print(liste3)
liste3[:2] = 1, 5  # 2 indekse kadar olan elemanları değiştirme.
print(liste3)

# Append ile Pop metodu
# ar = int(input("Sayı giriniz"))
# liste3.append(ar)
# print(liste3)
# liste3.pop(0)
# print(liste3)

#Sort metodu
newList = [1,7,9,2,4,6,2455,64327,45224,121231]
newList.sort()# newList.sort(reverse=True) Büyükten küçüğe
print(newList)

listlist = [newList],[liste3,[liste2]]
print(listlist)
