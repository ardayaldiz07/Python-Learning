print("""************
Kullanıcı Girişi Programı
************
""")

sys_kullanıcı_adı = "arda"
sys_parola = "12345"
giriş_hakkı = 3

while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    kullanıcı_parola = input("Parola: ")

    if giriş_hakkı > 0:
        if kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_parola != sys_parola:
            print("Hatalı kullanıcı adı ve parolası.")
            giriş_hakkı -= 1
        elif kullanıcı_adı != sys_kullanıcı_adı and kullanıcı_parola == sys_parola:
            print("Hatalı kullanıcı adı.")
            giriş_hakkı -= 1
        elif kullanıcı_adı == sys_kullanıcı_adı and kullanıcı_parola != sys_parola:
            print("Hatalı parola")
            giriş_hakkı -= 1
        elif kullanıcı_adı == sys_kullanıcı_adı and kullanıcı_parola == sys_parola:
            print("Sisteme giriş yapılıyor...")
            break
        if giriş_hakkı == 0:
            print("Lütfen daha sonra tekrar deneyin...")
            break
