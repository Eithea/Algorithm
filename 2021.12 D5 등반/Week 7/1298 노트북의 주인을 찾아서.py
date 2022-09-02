import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, k = map(int, input().split())
m = n
pref = [[] for i in range(n+1)]
match = [0 for i in range(m+1)]
visit0 = [False for i in range(n+1)]

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if not match[p] or DFS(match[p]) : 
            match[p] = now
            return True
    return False

count = 0
for i in range(k) : 
    x, y = map(int, input().split())
    pref[x].append(y)
for i in range(1, n+1) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1
print(count)