# 600851475143 sayısının en büyük asal carpanı nedir?
# What is the largest prime multiplier of the number 600851475143?

from allprimes import allprimes

primes=allprimes(10000)
number,i=600851475143,1
while not (number%primes[-i]==0):
    i += 1
print(primes[-i])
