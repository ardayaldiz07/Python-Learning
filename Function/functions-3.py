def Summon(a,b,c):
    return a+b+c
def Extension(d):
    return d*2    

sum = Summon(a = int(input("Sayı:")),b = int(input("Sayı:")), c = int(input("Sayı:")))    
print(Extension(sum))