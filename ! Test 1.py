from itertools import permutations
from collections import defaultdict

n, m = map(int, input().split())
l = list(map(int, input().split()))
comb = list(permutations(l, m))
print(comb)
V = defaultdict(int)
for sub in comb : 
    if V[sub] == 1 : 
        continue
    V[sub] = 1
    TF = True
    for i in range(m-1) : 
        if sub[i] < sub[i+1] : 
            TF = False
    if TF : 
        print(*sub)