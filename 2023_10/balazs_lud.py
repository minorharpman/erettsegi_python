# 1. feladat
osvenyek = []
with open("osvenyek.txt", "r") as f1:
    for sor in f1.readlines():
        osvenyek.append(sor.strip())

dobasok = []
with open("dobasok.txt", "r") as f2:
    for dobas in f2.readlines()[0].strip().split(" "):
        dobasok.append(dobas)


print("2. feladat")
print(f"A bobások száma: {len(dobasok)}")
print(f"Az ösvények száma: {len(osvenyek)}")


print("\n3. feladat")
leghosszabb = [0, 0]
for i in range(len(osvenyek)):
    if len(osvenyek[i]) > leghosszabb[1]:
        leghosszabb = [i+1, len(osvenyek[i])]

print(f"Az egyik leghosszabb a(z) {leghosszabb[0]}. ösvény, hossza: {leghosszabb[1]}")


print("\n4. feladat")
sorszam = int(input("Adja meg egy ösvény sorszámát! "))
jatekosok = int(input("Adja meg a játékosok számát! "))


print("\n5. feladat")
mezok = {}
for mezo in osvenyek[sorszam-1]:
    if mezo not in mezok.keys():
        mezok[mezo] = 1
    else:
        mezok[mezo] += 1
for k, v in mezok.items():
    print(f"{k}: {v} darab")


# 6. feladat
with open("kulonleges.txt", "w") as ujFajl:
    for i in range(len(osvenyek[sorszam-1])):
        if osvenyek[sorszam-1][i] != "M":
            ujFajl.writelines(f"{i+1}{chr(9)}{osvenyek[sorszam - 1][i]}\n")


print("\n7. feladat")
jatekos = 0
jatekos_dobasok = [[] for i in range(jatekosok)]
i = 0
tartozkodasok = [0, 0, 0, 0, 0]
while max(tartozkodasok) < len(osvenyek[sorszam-1]):
    jatekos_dobasok[jatekos].append(int(dobasok[i]))
    if jatekos < jatekosok-1:
        jatekos += 1
    else:
        jatekos = 0
    tartozkodasok = [sum(x) for x in jatekos_dobasok]
    i += 1
print(f"A játék a(z) {len(jatekos_dobasok[0])}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {tartozkodasok.index(max(tartozkodasok))+1}")


print("\n8. feladat")
mezok = osvenyek[sorszam-1]
jatekos = 0
jatek = True
jatekos_dobasok = [[] for i in range(jatekosok)]
nyertesek = []
i = 0
tartozkodasok = [0 for i in range(jatekosok)]
while max(tartozkodasok)+6 < len(mezok):
    jatekos_dobasok[jatekos].append(int(dobasok[i]))
    tartozkodasok[jatekos] += int(dobasok[i])
    if tartozkodasok[jatekos] >= len(mezok):
        jatek = False
    if jatek:
        if mezok[tartozkodasok[jatekos]] == "E":
            tartozkodasok[jatekos] += int(dobasok[i])
        elif mezok[tartozkodasok[jatekos]] == "V":
            tartozkodasok[jatekos] -= int(dobasok[i])
        if jatekos < jatekosok-1:
            jatekos += 1
        else:
            jatekos = 0
        i += 1
for i in range(len(tartozkodasok)):
    if tartozkodasok[i] == max(tartozkodasok):
        nyertesek.append(str(i+1))
print(f"A nyertes(ek) : {' '.join(nyertesek)}")
print("A többiek pozíciója:")
for i in range(len(tartozkodasok)):
    if str(i+1) not in nyertesek:
        print(f"{i+1}. játékos, {tartozkodasok[i]}. mező")

