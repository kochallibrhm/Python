#Listedeki sayılar tek ve cift olarak ayrılıyor
#Separates the numbers in the list as single and double

liste=[12,223,233,1212,744]
cift=[]
tek=[]
for i in liste:
    if i%2==0:
        cift.append(i)
    else:
        tek.append(i)
print(tek,cift)        
