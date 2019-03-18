#girilen sayının asal carpanları
#primed factors of the entered numbers

def carpan(n):
    liste=[1]
    i,m=2,n/2
    while(i<=m):
        if(n%i==0):
            liste.append(i)
            n=n/i
        else:
            i += 1
    return(liste)
print(carpan(100)) #parantez icindeki sayının carpanlarını verir
 
#asal sayıları bulmak icin bu satırları ekleyebiliriz
#for i in range(2,100):
#    if sum(carpan(i))==1:
#        print(i)
