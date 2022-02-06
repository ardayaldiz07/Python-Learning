# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = int(input("Sayı gir: "))
b = int(input("Sayı gir: "))
print(f"A nın değeri:{a}\nB nin değeri{b}")
a, b = b, a
print(f"A nın değeri:{a}\nB nin değeri{b}")