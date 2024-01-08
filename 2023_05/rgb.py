
#print("1. feladat ")
kep = open("kep.txt", "r")

Kep = kep.readlines()
#print('Kep',  Kep)

print("2. feladat ")
print("Kérem egy képpont adatait!")
sorSz = int(input("Sor: "))
oszlopSz = int(input("Oszlop : "))

adottSor = Kep[sorSz-1]
#print('adottSor',  adottSor)
adottSorList = adottSor.split(" ")
#print('adottSorList',  adottSorList)

rList = []
gList = []
bList = []
szamlalo = 0
while szamlalo < len(adottSorList):
    rList.append( adottSorList[szamlalo] )
    szamlalo +=1
    gList.append( adottSorList[szamlalo] )
    szamlalo += 1
    bList.append( adottSorList[szamlalo] )
    szamlalo += 1

#print( rList[oszlopSz-1])
#print( gList[oszlopSz-1])
#print( bList[oszlopSz-1])

print("A képpont színe RGB (", rList[oszlopSz-1],",", gList[oszlopSz-1],",",  bList[oszlopSz-1] , ")" )
