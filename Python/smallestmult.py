# 1 den 20 ye kadar olan sayıların hepsine tam bölünen en kücük sayı
# Smallest number divided by numbers from 1 to 20

i,j=2,2500
while i<21:
    if j%i==0:
        i += 1
    else:
        j += 1 
        i=2 
print(j)        
    
