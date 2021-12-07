import sys
input = sys.stdin.readline
from heapq import heappush, heappop
from bisect import bisect_left

n, k = map(int, input().split())

N = []
for i in range(n) : 
    weight, value = map(int, input().split())
    heappush(N, [-value, weight])

K = []
for i in range(k) : 
    K.append(int(input()))
used = [False for i in range(k)]
K.sort()

sumv = 0
while N : 
    Rvalue, weight = heappop(N)
    i = bisect_left(K, weight)
    while i < k and used[i] : 
        i = i + 1
    if i < k : 
        used[i] = True
        sumv = sumv - Rvalue
print(sumv)
