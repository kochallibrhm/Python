﻿# 10001 inci asal sayıyı bulan kod.
# 10001. prime number

from functions import isprime

n,p=0,1
while n<10001:
    p += 1
    if(isprime(p)==1):
        n += 1
print(p)
