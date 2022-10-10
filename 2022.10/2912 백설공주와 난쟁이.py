import sys
input = sys.stdin.readline

def range_in(x) : 
    distribution[x] += 1

def range_out(x) : 
    distribution[x] -= 1

n, k = map(int, input().split())
distribution = [0 for i in range(k+1)]

A = list(map(int, input().split()))

m = int(input())
Q = []
for i in range(m) : 
    l, r = map(int, input().split())
    Q.append([l-1, r-1, i])

sq = int(n**0.5)
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sq)
ans = [None for i in range(m)]


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
    mxd = max(distribution)
    if mxd > (r-l+1) //2 : 
        ans[i] = f"yes {distribution.index(mxd)}"
    else : 
        ans[i] = 'no'

print(*ans, sep = '\n')