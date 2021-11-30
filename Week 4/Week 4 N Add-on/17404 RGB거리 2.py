import sys
input = sys.stdin.readline

n = int(input())
C = []
for i in range(n) : 
    C.append(list(map(int, input().split())))

mx = sys.maxsize
DP = [[[mx, mx, mx] for i in range(n)] for i in range(3)]
minc = mx
for start in range(3) : 
    DP[start][0][start] = C[0][start]
    for i in range(1, n) : 
        for j in range(3) : 
            DP[start][i][j] = min(DP[start][i-1][j-1], DP[start][i-1][j-2]) + C[i][j]
    minc = min(minc, DP[start][n-1][start-1], DP[start][n-1][start-2])
print(minc)