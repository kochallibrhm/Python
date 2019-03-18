# İlk 100 dogal sayının kareleri toplamı ile toplamının karesi arası farkı
# The diffrence between first hundred natural numbers squares and these hundred numbers sums.

l=[] 
t=[]
for i in range(101):
    l.append(i)
    t.append(i)
for i in l:
    l[i]=i**2
print((sum(t)**2)-sum(l))
