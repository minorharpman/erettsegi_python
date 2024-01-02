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

#megoldás:
megtett = [0, 0, 0, 0, 0]
# osvenyt kell vegigjarni a jatekosvaltassal

print( "játékosok száma:" +str(jatekosSzam))


#Ez a lenti rész felejtős
lepesTarolo = []

# lépés LIST létrehozás [] elemmel, hogy lehessen hozzáadni
for jatekos in range(jatekosSzam) :
    lepesTarolo.insert(jatekos, [])

sorszam = 0
# lepesTarolo feltöltés
for i in range(0, len(DobasTomb), jatekosSzam):

    if( len(adottSorList) < sorszam ) : break
    #print (dobas)
    for jatekos in range(jatekosSzam) :
        lepteto = int(jatekos)+int(i)
        #print(lepteto)
        #védelem  IndexError: list index out of range
        try:
          lepesTarolo[jatekos].append(int(DobasTomb[lepteto]))
        except:
          print( "  ")

    sorszam += 5


'''
print(lepesTarolo[0])
print(lepesTarolo[1])
print(lepesTarolo[2])
print(lepesTarolo[3])
print(lepesTarolo[4])
'''

for sor in lepesTarolo:
    #print(sor)
    print ("sor: "+ str(sum(sor)) + " kör: " + str(int(len(sor)/jatekosSzam)))


print("8. feladat ")


