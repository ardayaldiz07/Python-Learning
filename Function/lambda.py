# liste1 = [1,2,3,4,5]

# liste2 = [i * 2 for i in liste1]
# print(liste2)

def ikiyleçarp(x):
    return x*2

ikiyleçarp2 = lambda x : x * 2

print(ikiyleçarp2(3))

toplama = lambda a,b,c : a + b + c

print(toplama(5,21,23))

tersçevir = lambda s : s[::-1]

print(tersçevir("Naber Müdür"))