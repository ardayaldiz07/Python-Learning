# Bu yerel
def fonksiyon():
    a = 10
    print(a)


fonksiyon()

# Bu global

b = 5


def fonksiyon2():
    print(b)


fonksiyon2()


c = 10


def fonksiyon3():
    c = 2
    print(c)


fonksiyon3()
print(c)

d = 10


def fonksiyon4():
    global d  # Çok kullanışlı değil
    d = 3
    print(d)


fonksiyon4()
print(d)

if True:
    e = 4
    print(e)
    
print(e)    
