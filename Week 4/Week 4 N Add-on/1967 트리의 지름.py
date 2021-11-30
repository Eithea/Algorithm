import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import defaultdict

Vn = int(input())
V = defaultdict(list)
child = [0 for i in range(Vn + 1)]
for i in range(Vn - 1) : 
    v1, v2, c = map(int, input().split())
    V[v1].append([v2, c])
    V[v2].append([v1, c])

DP = [0 for i in range(Vn + 1)]
def DFS(now) : 
    for next, cost in V[now] : 
        if DP[next] == 0 : 
            DP[next] = DP[now] + cost
            DFS(next)
DFS(1)
DP[1] = 0
x = DP.index(max(DP))
DP = [0 for i in range(Vn + 1)]
DFS(x)
DP[x] = 0
print(max(DP))