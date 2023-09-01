#run: py python_valtozok.py


print("Python oktatás - FREE BIRD Programozó Képző")
print("Műveletek változókkal\n\n")


print("Figyeljünk, hogy milyen típusú változókkal dolgozunk!\n")
a = 3

#b = 2
b = "4"
#b= int(b)

print("Az eredmény típusa: ", type(b))

c= a*b


print("Művelet eredménye: ", c)
print("Az eredmény típusa: ", type(c))

# tuple -rendezett véges lista, nem lehet hozzáadni elemeket, nem lehet módosítani
tanulok = ('Teri nagymama', 'Sanyi bácsi')
print("A tanulok típusa: ", type(tanulok))

#Ajánlott alap python videó:Lista és dictionary - Python alapjai
# https://www.youtube.com/watch?v=OkZGUakKgOw&ab_channel=PythonVil%C3%A1g

#lista, tömb
tanulok2 = [ 'Évi','Lali','Béla']
print("A tanulok2 típusa: ", type(tanulok2))

#szotar tipus
programozok = {'elso':'Zoli', 'masodik':'Peti'}
print("A programozok típusa: ", type(programozok))

#TypeError: can only concatenate tuple (not "list") to tuple
#emberek = tanulok + tanulok2

#emberek = list(tanulok) + tanulok2

#TypeError: can only concatenate list (not "dict") to list
#emberek = list(tanulok) + tanulok2 + programozok

# vigyázat, itt a programozok-nál az indexek kerülnek be!
#emberek = list(tanulok) + tanulok2 + list(programozok)

emberek = list(tanulok) + tanulok2 + list(programozok.values())

print("A emberek típusa ", type(emberek))   


for ember in emberek:
    print('ember: ', ember)



print("Típus ", type(emberek))    

