#rakamlarının 4. kuvvetleri toplamı kendisine esit olan sayılar (100,10000 arası)
#What is the numbers of the fourth forces of the numbers are equal to himself?(between 100 and 10000)

def kuvtop(n,p):
    toplam=0
    for i in str(n):
        toplam += int(i)**p
    return(toplam)
for i in range(100,10000):
    if(i==kuvtop(i,4)):  # 4 yerine farklı sayılar kullanılabilir
        print(i)
