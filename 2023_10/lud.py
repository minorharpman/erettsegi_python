print("Társas")

dobasok = open("dobasok.txt", "r")
# print (type(dobasok))
osvenyek = open("osvenyek.txt", "r")
# print (type(osvenyek))

print("2. feladat ")

Sorok = osvenyek.readlines()
# print (type(Lines))
print("Az ösvények száma: " + str(len(Sorok)))

DobasList = dobasok.readlines()
# első sorban vannak a dobások
DobasStr = DobasList[0]
# print(DobasStr)
# megint Tömb a számosság miatt
DobasTomb = DobasStr.split(" ")

print("A dobások száma: " + str(len(DobasTomb)))

print("3. feladat ")

sorszam = 1
legnSorhossz = 0
legnSorhosszSzama = 0
for sor in Sorok:
    sorhossz = len(sor)
    # print( sorszam, sorhossz)
    if sorhossz > legnSorhossz:
        legnSorhossz = sorhossz
        legnSorhosszSzama = sorszam
    sorszam += 1

print("Az egyik leghosszabb a(z) " + str(legnSorhosszSzama) + ". ösvény, hossza:" + str(legnSorhossz))

print("4. feladat ")

osvenySorszam = int(input("Adja meg egy ösvény sorszámát!: "))
jatekosSzam = int(input("Adja meg a játékosok számát! : "))

# print(osvenySorszam, jatekosSzam)

print("5. feladat ")

tenylegesSor = osvenySorszam - 1
adottSor = Sorok[tenylegesSor]
# print(adottSor)
# listát készít a stringből
adottSorList = list(adottSor)
# print(adottSorList)

szamM = 0
szamV = 0
szamE = 0
sorszam = 1

f = open("kulonleges.txt", "w", encoding="utf-8")

for elem in adottSorList:
    # print(elem)
    if (elem == "M"): szamM += 1
    if (elem == "V"):
        szamV += 1
        f.write("sorszám: " + str(sorszam) + " \t  típus: V, \n")

    if (elem == "E"):
        szamE += 1
        f.write("sorszám: " + str(sorszam) + " \t  típus: E, \n")

    sorszam += 1

print("M: " + str(szamM) + " darab ")
print("V: " + str(szamV) + " darab ")
print("E: " + str(szamE) + " darab ")

print("7. feladat ")

# 5 ember max, Egy ilyen alkalommal az öt unoka egy régi dobozra bukkant
megtett = [0, 0, 0, 0, 0]

# osvenyt kell vegigjarni a jatekosvaltassal

# print( "játékosok száma:" +str(jatekosSzam))

kor = 0
ut = 0

while ut < len(adottSorList):
    for jatekos in range(int(jatekosSzam)):
        # print('jatekos:', jatekos)
        # print(adottSorList[helySzam])
        dobas = DobasTomb[jatekos + kor * jatekosSzam]
        # print('jatekos:', jatekos, 'dobas', dobas)
        megtett[jatekos] = int(dobas) + megtett[jatekos]
        ut = megtett[jatekos]
    # print('jatekos:', jatekos, 'ut', ut)

    kor += 1

print(kor)
print('7', megtett)

leghosszabb = 0
jatekosIndex = 0
szamlalo = 0
for n in megtett:
    szamlalo += 1
    if (n > leghosszabb):
        leghosszabb = n
        jatekosIndex = szamlalo

print('A játék a(z) ', kor, '. körben fejeződött be. A legtávolabb jutó(k) sorszáma:',  jatekosIndex)


print("8. feladat ")

megtett = [0, 0, 0, 0, 0]

# osvenyt kell vegigjarni a jatekosvaltassal

# print( "játékosok száma:" +str(jatekosSzam))

kor = 0
maxtav = 0

print('ösvény hossza:', len(adottSorList))
while maxtav < len(adottSorList):
    for jatekos in range(int(jatekosSzam)):

        dobas = DobasTomb[jatekos + kor * jatekosSzam]
        #print('jatekos:', jatekos, 'dobas', dobas)
        megtett[jatekos] = int(dobas) + megtett[jatekos]

        # Igazítás V, E esetén
        if (megtett[jatekos] < len(adottSorList)):

            #print('jatekos:', jatekos, 'dobas', int(dobas), 'út', megtett[jatekos], 'tipus', adottSorList[maxtav], 'maxtav', maxtav)

            if (adottSorList[megtett[jatekos]-1] == 'E'):
                megtett[jatekos] = int(dobas) + megtett[jatekos]
                #print('jatekos:', jatekos, 'dobas', int(dobas), 'út', megtett[jatekos], 'tipus', adottSorList[maxtav],  'maxtav', maxtav)

            if (adottSorList[megtett[jatekos]-1] == 'V'):
                megtett[jatekos] = megtett[jatekos] - int(dobas)
                #print('jatekos:', jatekos, 'dobas', int(dobas), 'út', megtett[jatekos], 'tipus', adottSorList[maxtav],  'maxtav', maxtav)
        #ne vegtelen ciklusba menjen
        maxtav = max(maxtav, megtett[jatekos])

    kor += 1

print(kor)

print('ösvény hossza:', len(adottSorList))
print('8', megtett)

nyertesH = []
nyertesSz = []
tobbiH = []
tobbiSz = []
index =0
for n in megtett:
    #print( 'n index:', index)
    if (n >= len(adottSorList)):
        nyertesH.append(n)
        nyertesSz.append(index+1)
    else:
        tobbiH.append(n)
        tobbiSz.append(index+1)

    index +=1

print('nyertes szamú játékosok', nyertesSz, 'tobbi szamú jatékosok', tobbiSz)
print('nyertes hossz', nyertesH, 'tobbi hossz', tobbiH)