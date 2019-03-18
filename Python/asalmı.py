# Bir sayının asal olup olmadıgını kontrol eden fonksiyon
# A function that checks whether is the number is a prime or not

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
print(isprime(13)) #parantez icindeki sayı asalsa 1 değil ise 0 cıktı verir
