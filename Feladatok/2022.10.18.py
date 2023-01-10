"""import random
szam=int(input"Addj meg egy szamot")
veltipp=random.randit(1,100)
lepes=0
talalt=False

while talalt==False:
    if szam=veltipp:
        lepes+=1
        print(f"{lepes}-ből kitaláltad")
        talalt=True
    elif szam>veltipp:
        lepes+=1
        veltipp=random.randint(1, szam)

    elif szam<veltipp:
        lepes+=1
        veltipp=random.randint(szam. 100)

    else:
        print("Nem nyert!")
"""

#1feladat
"""
a=int (input("Adj meg egy számot"))
b=int (input("Add meg a masik szamot"))

print(f"A megoldas {a+b*2}")
"""

#2feladat
"""
a=int (input("Add meg a szamot"))
db=0

while a!=0:
    if a>5:
        db+=1
    a=int (input("Add meg a szamot"))
print(f"kiléptem a ciklusból: {db}")
"""
#3feladat
"""
a=int (input("Add meg a hőmérsékletet"))
osszeg=0
db=0
atlag=0

while a>0:
    a=int (input(f"Add meg a hőmérsékletet"))
    osszeg+=a
    db+=1

if db!=0:
    atlag=round(osszeg/db,1)

print(f"{atlag}")
"""

#4feladat
"""
a=int (input("Add meg a hőmérsékletet"))
osszeg=0
db=1

while a>-5:
    a=int (input("Add meg a hőmérsékletet"))

    if a>10:
        
        db+=1

print(f"{db}-db  10 C-nál nagyobbat adott meg")  
"""

#5feladat
"""
a=int (input("Add meg a számot"))
paros=0
paratlan=0

while a!=0:

    
    if a%2:
        a=int (input("Add meg a számot"))
        paros+=1
    else:
        a=int (input("Add meg a számot"))
        paratlan+=1
print(f"{paros}-paros,{paratlan}-paratlan")    
"""

#6feladat
"""

a=int (input("Add meg a számot"))

osszeg=a


while a!=0:
    a=int(input("Add meg a számot"))
    osszeg+=a

print(f"{osszeg}-az osszeg")  
"""

#7feladat
#SIMON! NEM JÓ EZ A FELADAT (ezt nem tudtam)   
"""
a=int(input("Add meg a számot"))
osszeg=0


while a!=0:
    b=int (input("Add meg a számot"))
    osszeg+=

print(f"Az osszeg:{osszeg}")"""


#10feladat

n=int(input("Sorok száma:"))
m=int(input("Oszlopok száma:"))
i=0

while i<n:
    j=0
    while j<2m:
        print("*", end="\t")
        j+=1
    print()
    i+=1


i=1:

while i<11:
    j=1
    while j<11:
        print(i*j, end="\t")
        j+=1
    print()
    i+=1    
     

