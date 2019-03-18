#Sıfırdan kullanıcıdan girilen n sayısına kadar bir dizi olusturup sol bastan baslayıp birer atlayarak elemanları cıkarıp son kalanı cıktı verir.
#Program that creates a sequence from zero to the n number entered from the user. And removes the elements one by one but the way like one removes, one stay and it's starts from the left head. And that process repeats until one element remains.

n=int(input("Bir sayı girin: " ))
liste=[]
for i in range(1,n+1):
    liste.append(i)
i=0
while(len(liste)!=1):
    liste[i]=0
    liste.remove(0)
    i=i+1
    print(liste)
    if i==len(liste):
       liste.reverse()
       i=0
    elif i==len(liste)+1:
        liste.reverse()
        i=0
