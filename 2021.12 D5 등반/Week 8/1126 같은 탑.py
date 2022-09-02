n = int(input())
L = list(map(int, input().split()))
DP = [[-1 for i in range(sum(L)+1)] for i in range(n+1)]
DP[0][0] = 0
maxh = 0
for now in range(1, n+1) : 
    h = L[now-1]
    maxh = maxh + h
    for gap in range(maxh+1) : 
        if DP[now-1][gap] == -1 : 
            continue
        DP[now][gap + h] = max(DP[now][gap + h], DP[now-1][gap] + h)
        DP[now][gap] = max(DP[now][gap], DP[now-1][gap])
        if gap >= h : 
            DP[now][gap - h] = max(DP[now][gap - h], DP[now-1][gap])
        else : 
            DP[now][h - gap] = max(DP[now][h - gap], DP[now-1][gap] + h - gap)
ans = DP[n][0]
if ans : 
    print(DP[n][0])
else : 
    print(-1)