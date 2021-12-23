import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
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

spec = [[] for i in range(n+1)]
for i in range(1, n+1) : 
    spec[i] = list(map(int, input().split()))
for i in range(1, n) : 
    for j in range(i+1, n+1) : 
        if spec[i][0] <= spec[j][0] and spec[i][1] <= spec[j][1] and spec[i][2] <= spec[j][2] : 
            pref[j].append(i)
        elif spec[i][0] >= spec[j][0] and spec[i][1] >= spec[j][1] and spec[i][2] >= spec[j][2] : 
            pref[i].append(j)

count = 0
for i in range(1, n+1) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1
for i in range(1, n+1) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1
print(n - count)