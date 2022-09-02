import sys
input = sys.stdin.readline

n = int(input())
T = [[] for i in range(n)]
for i in range(n) : 
    T[i] = list(map(int, input().split()))

DP = [[0 for i in range(n)] for i in range(n)]
DP[0][0] = T[0][0]
for i in range(1, n) : 
    DP[i][0] = DP[i-1][0] + T[i][0]
    for j in range(1, i+1) : 
        DP[i][j] = max(DP[i-1][j-1] + T[i][j], DP[i-1][j] + T[i][j])

print(max(DP[-1]))