"""#Simon! Ez a mai óra.

honapok=["január","február","március","április","május","június"]
print(honapok)
print(','.join(honapok))
print(len(honapok))
print(honapok[0])
print(honapok[len(honapok)-1])
print(honapok[1:5])
print(honapok[1:])
print(honapok[:4])
print(honapok[::-2])
print(honapok[-2:-6:-1])
for honapok in honapok:
    print(honapok)

for index in range(len(honapok)):
    print(index,honapok[index])

for index, honapok in enumerate(honapok,start=1):
    print(index)





ho_masolat=honapok
print(ho_masolat)
print(sorted(honapok))
print(honapok)



honapok.extend(uj_honapok)
import random
"""


import random
szamok=[] #üres lista
for i in range(5):
    szamok.append(random.randit(1,99))
print(szamok)
print(min(szamok))
print(max(szamok))
print(sum(szamok))









szamok1=[]
for i in range(5):
    szamok.append(random.randit(1,99))
ij_szamok=szamok+szamok1
print(uj_szamok)
print(szamok*3)



eredmeny=[x*2 for x in sazmok]
print(eredmeny)
eredmeny1[X**2 for x in szamok if x%2==0]
print(eredmeny)































