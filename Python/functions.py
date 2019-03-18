# Bir sayının asal olup olmadıgını kontrol eden fonksiyon
# İs pandigital

def isprime(a):
    i,prime=3,1
    if a!=2 and a%2==0:
        prime=0
    while prime!=0 and i<=a**(1/2):
        if a%i==0:
            prime=0
            break
        i += 2
    return(prime)


# Bir sayıdan kücük bütün asal sayıları dizi olarak döndüren fonksiyon
# Function that returns all prime numbers up to a number as an array
def allprimes(n):
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
         if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])


# Bir sayının pandigital olup olmadığını kontrol eden fonksiyon
# is pandigital

def ispandigital(n):
    number = []
    for i in str(n):
        number.append(int(i))
    for i in range(1,len(number)+1):
        if(number.count(i)==0):
            return(0)
            break
    else:
        return(1)
