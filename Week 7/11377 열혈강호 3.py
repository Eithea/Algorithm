import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m, k = map(int, input().split())
pref = [[] for i in range(n+1)]
match = [0 for i in range(m+1)]
visit0 = [False for i in range(n+1)]

def countnon0(match) : 
    count = 0
    for i in match : 
        if i : 
            count = count + 1
    return count

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if not match[p] or DFS(match[p]) : 
            match[p] = now
            return True
    return False

for i in range(1, n+1) : 
    l = list(map(int, input().split()))
    for p in range(l[0]) : 
        pref[i].append(l[p+1])

count = 0
for i in range(1, n+1) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1

for i in range(1, n+1) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1
        k = k - 1
        if not k : 
            break
print(count)