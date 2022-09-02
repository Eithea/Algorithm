n, k = map(int, input().split())

must = ['a', 'n', 't', 'i', 'c']

l = [0 for j in range(n)]
for i in range(n) : 
    lt = input()
    for j in range(len(lt)) : 
        if lt[j] not in must : 
            l[i] = l[i] | 1 << (ord(lt[j])-97)

if k < 5 : 
    print(0)
    exit(0)

alph = [i for i in range(26)]
for a in must : 
    alph.remove(ord(a)-97)

from itertools import combinations
cases = list(combinations(alph, k-5))

maxc = 0
for case in cases : 
    x = 0
    count = 0
    for d in case : 
        x = x | 1 << d
    for word in l : 
        if word & x == word : 
            count += 1
    maxc = max(maxc, count)

print(maxc)