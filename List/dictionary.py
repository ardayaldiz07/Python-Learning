sözlük1 = {"Freedom":"Özgürlük","Happy":"Mutlu"}
print(sözlük1["Freedom"])
sözlük1["Modest"] = "Mütevazı"
print(sözlük1)

sözlük2={"bir":[1,2,3],"iki":[[123,456]]}
print(sözlük2["iki"][0][0])

sözlük2["bir"] = [0]
print(sözlük2)

print(sözlük2.keys())
print(sözlük2.values())
print(sözlük2.items())

for k,v in sözlük2.items():
    print(k,v)     