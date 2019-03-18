#kullanıcıdan girilen k sayısına kadar kac tane asal sayı var
#how many prime numbers are available from user to n
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
k=int(input("Bir sayı girin: "))
asal=[]
for i in range(2,k+1):
    if sum(carpan(i))==1:
        asal.append(i)
print(len(asal))
