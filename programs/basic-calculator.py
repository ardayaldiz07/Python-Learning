print("""***************
Hesap Makinesi Programı

İşlemler;

1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme



***************
""")


operator = int(input("İşlem giriniz: "))
number1 = int(input("Birinci Sayıyı Giriniz: "))
number2 = int(input("İkinci Sayıyı Giriniz: "))


if operator == 1:
    print(f"{number1} ile {number2} toplamı {number1+number2}")
elif operator == 2:
    print(f"{number1} ile {number2} çıkarması {number1-number2}")
elif operator == 3:
    print(f"{number1} ile {number2} çarpması {number1*number2}")
elif operator == 4:
    print(f"{number1} ile {number2} bölmesi {number1/number2}")
else:
    print("Geçersiz İşlem")