from itertools import permutations, combinations, product, combinations_with_replacement

p = 1000000007
# 팩토리얼
F = [1 for i in range(4000001)]
for i in range(1, 4000001) : 
    F[i] = F[i-1] * i %p