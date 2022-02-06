liste1 = [1,2,3,4,5]

liste2 = list()

for i in liste1:
    liste2.append(i)
print(liste2)    

# Şimdi list comprehension

liste3 = [1,2,3,4,5]

liste4 = [i for i in liste3]
print(liste4)

liste5 = [3,4,5]

liste6 = [i*2 for i in liste5]
print(liste6)

liste = [(1,2),(3,4),(5,6)]

listeyeni = [i*j for i,j in liste]
print(listeyeni)

s = "Python"

listestring = [i*3 for i in s]
print(listestring)

listelist = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
listeliste2 = []
for i in listelist:
    for x in i:
        
        print(x)


listelist = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
listeliste2 = [x for i in liste for x in i]