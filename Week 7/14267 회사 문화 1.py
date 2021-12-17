import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
l = list(map(int, input().split()))

parent = [0 for i in range(n+1)]
child = [[] for i in range(n+1)]
for i in range(1, n+1) : 
    if l[i-1] > 0 : 
        parent[i] = l[i-1]
        child[l[i-1]].append(i)
    else : 
        boss = i

DP = [0 for i in range(n+1)]
def DFS(now) : 
    DP[now] = DP[now] + DP[parent[now]]
    for next in child[now] : 
        DFS(next)

for i in range(m) : 
    start, size = map(int, input().split())
    DP[start] = DP[start] + size
        
DFS(boss)
print(*DP[1:])