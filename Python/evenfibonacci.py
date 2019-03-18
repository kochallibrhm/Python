# 4 milyondan kücük cift fibonacci sayılarının toplamı
# Total sum of the double fibonacci numbers smaller than 4 million

a,b,c,toplam=1,1,0,0
while c<4000000:
    if c%2==0:
        toplam=toplam+c
    c=a+b
    a,b=b,c
print(toplam)
