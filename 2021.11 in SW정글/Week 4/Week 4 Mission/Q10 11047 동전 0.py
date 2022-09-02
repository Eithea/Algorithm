import sys
input = sys.stdin.readline
from math import gcd

n, k = map(int, input().split())
C = []
lcm = 1
maxc = 0
for i in range(n) : 
    c = int(input())
    C.append(c)
    lcm = lcm * c // gcd(lcm, c)
    maxc = max(maxc, c)

cycle = lcm // maxc
cycnt = (k // lcm) * cycle
k = k % lcm
count = [0 for i in range(k + 1)]
for now in range(1, k + 1) : 
    before = []
    for coin in C : 
        if coin <= now and count[now - coin] != -1:
            before.append(count[now - coin])
    if not before : 
        count[now] = -1
    else:
        count[now] = min(before) + 1
print(cycnt + count[k])