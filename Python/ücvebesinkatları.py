#1000 in altındaki 3 ve 5 in katları olan sayıların toplamı
#Multiples of 3 and 5 less then 1000

liste=[]
for i in range(1,1000):
    if i%3==0 or i%5==0:
        liste.append(i)
print(sum(liste))    
