import sys
input = sys.stdin.readline

n, k = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

f = [[0 for i in range(sum(V) + 1)] for i in range(n)]
minv = sum(V)
for i in range(n) : 
    w, v = W[i], V[i]
    for j in range(1, sum(V) + 1) : 
        if j >= v : 
            f[i][j] = max(f[i-1][j], f[i-1][j - v] + w)
        else : 
            f[i][j] = f[i-1][j]
        if f[i][j] >= k : 
            minv = min(minv, j)
print(minv)