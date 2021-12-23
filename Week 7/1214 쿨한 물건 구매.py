from math import gcd, ceil

d, p, q = map(int, input().split())

g = gcd(p, q)
if g * (p//g - 1) * (q//g - 1) <= d : 
    print(g * ceil(d/g))
    exit(0)

if p > q : 
    p, q = q, p

minc = ceil(d/q) * q
for i in range(ceil(d/q)) : 
    j = max(0, ceil((d - q * i) / p))
    minc = min(minc, q * i + p * j)
print(minc)