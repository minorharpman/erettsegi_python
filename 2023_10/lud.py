
print("Társas")

dobasok = open("dobasok.txt", "r")
#print (type(dobasok))
osvenyek = open("osvenyek.txt", "r")
#print (type(osvenyek))

print("2. feladat ")

Sorok = osvenyek.readlines()
#print (type(Lines))
print("Az ösvények száma: " + str(len(Sorok)))

DobasList = dobasok.readlines()
#első sorban vannak a dobások
DobasStr = DobasList[0]
#print(DobasStr)
#megint Tömb a számosság miatt
DobasTomb = DobasStr.split(" ")

print("A dobások száma: " + str(len(DobasTomb)))

print("3. feladat ")

sorszam  =1
legnSorhossz = 0
legnSorhosszSzama = 0
for sor  in Sorok:
    sorhossz = len(sor)
   # print( sorszam, sorhossz)
    if sorhossz > legnSorhossz:
        legnSorhossz = sorhossz
        legnSorhosszSzama = sorszam
    sorszam+= 1

print( "Az egyik leghosszabb a(z) " + str(legnSorhosszSzama)+". ösvény, hossza:" + str(legnSorhossz) )





