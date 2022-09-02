from itertools import permutations
from collections import defaultdict

n, m = map(int, input().split())
l = [i+1 for i in range(n)]
comb = list(permutations(l, m))
comb.sort()
V = defaultdict(int)
for sub in comb : 
    if V[sub] == 1 : 
        continue
    V[sub] = 1
    TF = True
    for i in range(m-1) : 
        if sub[i] > sub[i+1] : 
            TF = False
    if TF : 
        print(*sub)