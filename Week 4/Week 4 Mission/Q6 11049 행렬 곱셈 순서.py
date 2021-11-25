import sys
input = sys.stdin.readline

n = int(input())
M = []
for i in range(n) : 
    M.append(list(map(int, input().split())))

max = sys.maxsize
DP = [[max for i in range(n)] for i in range(n)]
for i in range(n) : 
    DP[i][i] = 0
for len in range(1, n) : 
    for i in range(n) : 
        if i + len < n : 
            for cut in range(len) : 
                DP[i][i + len] = min(DP[i][i + len], DP[i][i + cut] + DP[i + cut + 1][i + len] + M[i][0] * M[i + cut][1] * M[i + len][1])

print(DP[0][n-1])