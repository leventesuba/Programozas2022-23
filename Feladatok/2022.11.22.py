"""from itertools import count
import random
lista=[] #üres lista
for i in range(10): #10 számot generál
    lista.append(random.randint(1,1000))
print(lista)"""
"""lista.insert(4,50) #bővítés az ötödik helyre 50-est
print(len(lista)) #len hogya listaba mennyi elem van
print(lista.index(50)) #hanyadik helyen található az 50
print(lista.count(50)) #hány db 50 szám van
print(lista.remove(50)) #kitörli az 50-et"""

"""print(lista[::-1]) #forditrott sorrendbe kiiras
print(lista[1:8:2]) #masodikat kiirja 1-8 elemig
print(lista[-3:-8:-1]) #7-tol 3-ig
print(sum(lista)) #összeadja a listat
print(sum(lista)/len(lista)) #a lista elemeinek átlagát
for i in lista:
    if i%11==0 and i>100 or i%11==0:  #azonos számjegyű elemek kiiratása
        print(i)
db=0
for i in lista:
    if i>9 and i<100:    #kiira a 9-100 ig a kétjegyu szamok darabszamatr
        db+=1
        print(db)
"""
"""print(len([x for x in lista if x>9 and x<100])) """#kiirja a 9-100 ig a ketjegyu szamokat szama
"""print(count([x for x in lista if x>9 and x<100]))"""  #ez nem jo
"""print([x**2 for x in lista if x<10 ]) #az egyjegyu szamok negyzetei
print(sum([x for x in lista if x%3==0])) #kiirja a 3-al oszthato szamok osszeget
print(len([x for x in lista if x%10==0])) #kiirja a 0-val vegzodo szamok darabszamat
print(max([x for x in lista if x%5==0]))  #kiirja az 5-el oszthato szamok legnagyobb szamat
print(len([x for x in lista if x>500 and x<1000])) #haromjegyu 500-nal nagyobb 
print(sum([x for x in lista if x>-10 and x<10])) #egyjegyu szamok osszeget irja ki
print(sorted([x for x in lista if x>9 and x<100])) #novekvo sorrendbe a ketjegyu szamokat
print(sorted([x for x in lista if x%3==0])[::-1]) #csokkeno sorrendbe a 3-al oszrthato szamokat
""" 


"""#Vmi string
mondat=input("Mondat:") #bekér egy mondatot
print(mondat.count(" ")+1) #hany szobol all
print(len(mondat)) #hany betu
#maganhangzok
mgh=["a","á","e","é","o"]
db=0
for i in mondat:#vegigmegyek a listan
    if i in mgh:
        db+=1
print(db)
#tobbszorr egymas utan kiirja

mennyiszer=int(input("Hányszor:"))
print((mondat+" ")*mennyiszer) #(mondat+" ")-ez szoközt tesz bele
"""
mondat=input("Mondoat: ")
szo=input("Szó: ")
ind=mondat.index(" ") #index-el meghatározod hog hol talalhato az elso szokoz
elso=(mondat[:ind+1]+szo) #elso reszt hatrarozza meg #a "+1"-azert van h benne legyen a szokoz is
masod=mondat[ind:]
print(elso+masod)
