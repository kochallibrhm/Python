# Girilen say�ya kadar olan fibonacci dizisindeki say�lar
# Numbers in the fibonacci sequence smaller than the entered number 

n=int(input("Kacinci fibonacci sayisini istiyorsunuz: "))
fib1,fib2=1,1
for i in range(n-2):
    fib=fib1+fib2
    fib1,fib2=fib2,fib
print(fib)


