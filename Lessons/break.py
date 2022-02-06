from time import sleep


i = 1

# while (i<=10):
#     print("i:",i)
#     i+=1


# while (i<=10):
#     if (i == 5):
#         break
#     print("i:",i)
#     i += 1    

# liste = [1,2,3,4,5,6]

# for i in liste:
#     if (i == 3):
#         break
#     print("i:",i)

while True:
    name = input("İsminizi Giriniz(Çıkmak için 'q' ya basınız.): ")
    if (name == "q"):
        print("Programdan çıkılıyor...")
        break
    print("İsminiz: ",name)
