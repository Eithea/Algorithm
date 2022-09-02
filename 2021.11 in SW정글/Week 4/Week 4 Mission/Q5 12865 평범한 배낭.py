import sys
input = sys.stdin.readline

n, k = map(int, input().split())
C = []
for i in range(n) : 
    C.append(list(map(int, input().split())))
f = [[0 for i in range(k + 1)] for i in range(n)]

for i in range(n) : 
    w, v = C[i][0], C[i][1]
    for j in range(1, k + 1) : 
        if j >= w : 
            f[i][j] = max(f[i-1][j], f[i-1][j - w] + v)
        else : 
            f[i][j] = f[i-1][j]
print(f[n-1][k])