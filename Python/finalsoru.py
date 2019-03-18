# 1 den 1001 e kadar olan sayıların karelerinin ilk ve son rakamı toplamlarını veren kod
# The first and last digit of the squares of numbers from 1 to 1001

def toplam(n):
    l=list(str(n))
    t=int(l[-1])+int(l[0])
    return(t)
liste=[]
for i in range(1002):
    liste.append(i**2)
for i in liste:
    liste[i]=toplam(i)
print(sum(liste))
