# Birden n e kadar n tane sayının toplamı bir ücgensel sayıdır mesela 1+2+3 = 6 ücüncü ücgensel sayı 6 dır
# Finds the triangular numbers
def carpan(n):
    liste=[1]
    i=2
    while(i>=n):
        if(n%i==0):
            liste.append(i)
        else:
            i += 1
    return(liste)
k=1
toplam=0
while len(carpan(toplam))<=5:
    for t in range(1,k+1):
        toplam += t
    k += 1
print(toplam)     
