"""a=int(input(f"Ajd meg egy egész  számot"))
if a%5=0 and a%3==0:
    print(f"fizzbuzz")

elif a%3==0:
    print(f"fizz")

elif a%5==0:
    print(f"buzz")

else:
    print(f"Nem osztható se 3-mal se 5-el")
"""

"""import random
gondolt_szam=random.randint(1,100)
tipp=int(input("szám:"))
lepes=0
kitalaltad=False
while kitalaltad==False:
    if tipp==gondolt_szam:
        lepes+=1
        #lepes=lepes+1, megszámlálás
        print(f"{lepes}-ből találtad ki")
        kitalaltad=True
    elif tipp>gondolt_szam :
        print("Adj kisebb számot")
        lepes+=1
        tipp=int(input())
    elif tipp<gondolt_szam :
        print("Adj nagyobb számot")
        lepes+=1
        tipp=int(input())     
    else:
        print("Rossz")
        """



#Én adok meg egy számot és a gép találja ki hogy melyik szám, úgy hogy utasításokkal segítem a gépet
# 1-100-ig kérem a ciklusváltozókat
"""i=100 #kezdőérték a ciklusváltozóknak
while i>0:
    if i%2==1:
        print(i, end=";")
    i-=1"""


from re import I


n=int(inout("Kérem a számot")) 
i=1  
fakt=1
while i<=n:
    fakt=fakt*i
    i+=1
print(fakt)









