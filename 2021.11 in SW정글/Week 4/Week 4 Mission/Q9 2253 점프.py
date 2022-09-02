import sys
input = sys.stdin.readline

n, m = map(int, input().split())
TF = [True for i in range(n + 1)]
for i in range(m) : 
    TF[int(input())] = False

jump = int((2 * n - 2) ** 0.5) + 1
DP = [[n for i in range(jump + 1)] for i in range(n + 1)]

DP[1][0] = 0
for i in range(2, n+ 1) : 
    if TF[i] : 
        jump = int((2 * i - 2) ** 0.5)
        for j in range(1, jump + 1) : 
            if i > j : 
                DP[i][j] = min(DP[i-j][j-1], DP[i-j][j], DP[i-j][j+1]) + 1

ans = min(DP[n])
if ans == n : 
    print(-1)
else : 
    print(ans)