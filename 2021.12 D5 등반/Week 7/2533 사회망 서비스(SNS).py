import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
V = [[] for i in range(n+1)]
for i in range(n-1) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    V[v2].append(v1)

visit = [False for i in range(n+1)]
DP = [[0, 0] for i in range(n+1)]
def DFS(now) : 
    visit[now] = True
    DP[now][0] = 1
    for next in V[now] : 
        if not visit[next] : 
            DFS(next)
            DP[now][0] = DP[now][0] + min(DP[next])
            DP[now][1] = DP[now][1] + DP[next][0]
start = 1
DFS(start)
print(min(DP[start]))