#100 den kücük a ve b sayılarının, a**b seklinde en büyük basamak degeri toplamı 
#What is the sum of the largest digit value in the a**b form? numbers a and b smaller than 100.

sonuc=1
maxa,maxb=1,1
for a in range(2,100):
    for b in range(2,100):
        c=a**b
        toplam=0
        for i in str(c):
            toplam += int(i)
        if(toplam>sonuc):
            sonuc=toplam
            maxa,maxb=a,b
print(sonuc,maxa,maxb,maxa**maxb,len(str(maxa**maxb)))
