from itertools import product
from collections import defaultdict
n, m = map(int, input().split())
l = [i+1 for i in range(n)]
comb = list(product(l, repeat = m))
comb.sort()
V = defaultdict(int)
for sub in comb : 
    if V[sub] == 1 : 
        continue
    V[sub] = 1
    print(*sub)