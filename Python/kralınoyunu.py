#Kral n kadar kisi yuvarlak olusturup birine kılıcı verip yanındakini öldürmesini ister son kisi kalana kadar oyun devam eder

liste=[]
n=int(input("Oyun kac kisiyle oynansin: "))
for i in range(1,n+1):
    liste.append(i)
i=1
while(len(liste)!=1):
    liste[i%len(liste)]=0
    liste.remove(0)
    print(liste)
    i=(i+1)%len(liste)
print(liste)
