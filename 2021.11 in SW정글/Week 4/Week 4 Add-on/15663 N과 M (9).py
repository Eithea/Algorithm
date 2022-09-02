from itertools import permutations
from collections import defaultdict

n, m = map(int, input().split())
l = list(map(int, input().split()))
comb = list(permutations(l, m))
comb.sort()
V = defaultdict(int)
for sub in comb : 
    if V[sub] == 1 : 
        continue
    V[sub] = 1
    print(*sub)