import sys
input = sys.stdin.readline
from collections import defaultdict


distribution = defaultdict(int)
value = 0

def value_in(x) : 
    global value
    value += x * distribution[x] **2

def value_out(x) : 
    global value
    value -= x * distribution[x] **2

def range_in(x) : 
    value_out(x)
    distribution[x] += 1
    value_in(x)

def range_out(x) : 
    value_out(x)
    distribution[x] -= 1
    value_in(x)


n, k = map(int, input().split())
A = list(map(int, input().split()))
for x in A : 
    distribution[x] = 0

Q = []
for i in range(k) : 
    l, r = map(int, input().split())
    Q.append([l-1, r-1, i])

sq = int(n**0.5)
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sq)
ans = [None for i in range(k)]


pl, pr = Q[0][0], Q[0][0] -1
for l, r, i in Q : 
    while l > pl : 
        range_out(A[pl])
        pl += 1
    while l < pl : 
        pl -= 1
        range_in(A[pl])
    while r < pr : 
        range_out(A[pr])
        pr -= 1
    while r > pr : 
        pr += 1
        range_in(A[pr])
    ans[i] = value

print(*ans)