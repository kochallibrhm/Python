# a+b+c=1000 ve a**2 + b**2 = c**2 olan sayılar
# Numers in a+b+c=1000 ve a**2 + b**2 = c**2 form

for a in range(1,400):
    for b in range(a+1,400):
        c=1000-a-b
        if(a**2+b**2==c**2):
            print(a*b*c)
            break
