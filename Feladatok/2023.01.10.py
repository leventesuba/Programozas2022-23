"""# Szótár-statisztika

e=[1,2,1,2,1,1,2]
import random
lista=[]
for i in range(10):
    lista.append(random.randint(1,10))
szotar={}
for i in lista:
    if i in szotar:
        szotar[i]+=1
    else:
        szotar[i]=1
#kiírás
for kulcs, ertek in szotar.items():
    print(f"{kulcs}-{ertek} db")
print(set(lista))"""


"""import random

fuvar=[]

for i in range(10):
    fuvar.append(random.randint(1,10))
print(fuvar)

print(f"{sum(fuvar)} piculaja latt aznap osszesen  ")

print(f"{sum(fuvar)/(len(fuvar))} piculat keres atlagosan egy fuvarrqal ")


if 5 in fuvar:
    print(f"A taxisnak volt otpiculas beverteli fuvarja")
else:
    print(f"A taxisnak nem votl otpiculas bevetelu fuvarja")


"""print(f"{(fuvar.index(5))+1}  eleme volt az otpiculas bevetel ")"""

if 5 in fuvar:
    print(f"{(fuvar.index(5))+1} eleme volt az otpiculas")
else:
    print(f"A taxisnak nem votl otpiculas bevetelu fuvarja")
db=0
for i in fuvar:
    if i==5:
        db+=1
    else:
        db=db
print(f"{db} darab otpiculas bevetele volt")
print(f"{max(fuvar)} volt a legjobb fuvarja a taxisnak")"""


#róka
import random
libak=[]

for i in range(5):
    libak.append(random.randint(1,7))

farkas=[]
roka=[]

for i in libak:
    if i>3:
        farkas.append(i)
    else:
        roka.append(i)

print(roka)
print(f"{sum(roka)} kg libat ehet meg a roka")
print(f"{sum(roka)/len(roka):.1f} kg os libat eszik a roka atlagban ")

if i>=3 in libak:
    print(f"Előfordult")
else:
    print(f"Nem fordult elo")






