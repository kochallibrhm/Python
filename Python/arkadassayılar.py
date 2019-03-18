#2 ile 10000 arasındaki arkadaş sayılar
#Friend numbers between 2 and 1000

def carpan(n):
    liste=[1]
    i=2
    while(i<=n/2):
        if(n%i==0):
            liste.append(i)
        i += 1
    return(liste)
#toplam=0 eger toplamı istersek bu satırları devreye sokabiliriz
for i in range(2,10000):
    b=sum(carpan(i))
    if(i!=b and i==sum(carpan(b))):
        #toplam += i 
        print(i)
#print(toplam)
