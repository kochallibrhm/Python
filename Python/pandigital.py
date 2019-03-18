# Bir sayının pandigital olup olmadıgını kontrol eden fonksiyon
# Function that checks whether is the number pandigital or not

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
