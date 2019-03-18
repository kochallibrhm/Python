# İki tane üc basamaklı sayının carpımından elde edilen en büyük palindrom sayısı
# The largest number of palindrome numbers obtained from the bumps of two three-digit digits

palindrome=[]
for i in range(100,1000):
    for j in range(100,1000):
        if(str(i*j)==str(i*j)[::-1]):
            palindrome.append(i*j)
print(max(palindrome))
