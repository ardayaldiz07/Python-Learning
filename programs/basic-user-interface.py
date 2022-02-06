print("""****************
Kullanıcı Girişi.
****************
""")

sys_user_name = "Ardayldz"
sys_password = "12345"

user_name = input("Kullanıcı adı giriniz: ")
password = input("Şifrenizi giriniz: ")

if user_name == sys_user_name and password != sys_password:
    print("Hatalı Şifre...")
elif user_name != sys_user_name and password == sys_password:
    print("Hatalı Kullanıcı Adı...")
elif user_name != sys_user_name and password != sys_password:
    print("Bilgiler Hatalı...")   
else:
    print("Sisteme Başarıyla Giriş Yaptınız...")           