import random
lista=[]
db=0
for i in range(10):
    lista.append(random.randint(1,100))
print(lista)
osszeg=0
for i in lista:
    if i>50:
        osszeg+=i
        db+=1
print(f"A lista elemeinek összege: {osszeg}, dardab: {db}")
print(sum([x for x in lista if x>50]))
print(len([x for x in lista if x>50]))
n=len(lista)
i=0
while i<n and lista[i]!=50:
    i=i+1
print(f"Helye: {i}")
print("Vsn benne 50-es" if i<n else "Nincs benne")
print("Van benne 50-es, helye: {i}" if i<n else "Nincs benne")



paros=[]
paratlan=[]
for i in lista:
    if i%2==0:
        paros.append(i)
    else:
        paros.append(i)
print(paros)
print(paratlan)
max=lista[0]
min=lista[0]
maxi=0
mini=0
for i in range(len(lista)):
    if lista[i]>max:
        max=lista[i]
        maxi=1
    if lista[i]<min:
        min=lista[i]
        mini=1
print(f"Legnagyobb elem: {max}, helye: {maxi}")
print(f"Legkisebb elem: {min}, helye: {mini}")
for i in range(len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i]<lista[j]:#kacsacsor megforditasa----visszafele fogja(csokkeno sorrend)
            csere=lista[i]
            lista[i]=lista[j]
            lista[j]=csere
print(lista)  


"""t= [3,8,2,4,5,1,6]
n=len(t)
ker=5
i=0
while i<n and t[i] !=ker:
    i=i+1
if i<n: print("Van ilyen:", ker)
else: print("nincs ilyen elem:", ker)"""