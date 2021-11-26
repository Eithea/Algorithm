import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
W = []
for i in range(n) : 
    W.append(list(map(int, input().split())))

max = sys.maxsize
DP = [[max for i in range(1<<n)] for i in range(n)]

def DFS(start, now, excluded) :
    if DP[now][excluded] != max : 
        return DP[now][excluded]     
    if excluded == (1<<n) - 1 : 
        if W[now][start] != 0 : 
            DP[now][excluded] = W[now][start]
            return DP[now][excluded]
        else : 
            return max
    for next in range(n) : 
        if next != now and W[now][next] != 0 and not excluded & 1<<next : 
            DP[now][excluded] = min(DP[now][excluded], DFS(start, next, excluded | 1<<next) + W[now][next])
    return DP[now][excluded]

print(DFS(0, 0, 1))