import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
l = list(map(int, input().split()))

odd = []
even = []
for i in l : 
    if i %2 : 
        odd.append(i)
    else : 
        even.append(i)
if len(odd) != len(even) : 
    print(-1)
    exit(0)

rng = 2002
eratos = [1 for i in range(rng + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(rng ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, rng + 1, i) : 
            eratos[j] = 0


pref = [[] for i in range(n//2)]
first = l[0]
if first %2 : 
    V1 = odd
    V2 = even
else : 
    V1 = even
    V2 = odd
for i in range(n//2) : 
    for j in range(n//2) : 
        if eratos[V1[i] + V2[j]] : 
            pref[i].append(j)

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if match[p] == -1 or DFS(match[p]) : 
            match[p] = now
            return True
    return False

visit0 = [False for i in range(n//2)]
visit0[0] = True
ans = []
for x in pref[0] : 
    match = [-1 for i in range(n//2)]
    match[x] = 0
    count = 1
    for i in range(1, n//2) : 
        visit = visit0[:]
        if DFS(i) : 
            count = count + 1
    if count == n//2 : 
        ans.append(V2[x])
if ans : 
    ans.sort()
    print(*ans)
else : 
    print(-1)