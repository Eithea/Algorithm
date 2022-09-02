import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if not match[p] or DFS(match[p]) : 
            match[p] = now
            return True
    return False

c, d, v = map(int, input().split())
C = [[]]
D = [[]]
for i in range(v) : 
    x, y, z = input().split()
    if z == '0' : 
        C.append([int(x), int(y)])
    elif z == '1' : 
        D.append([int(x), int(y)])

n = len(C)
m = len(D)
pref = [[] for i in range(n)]
match = [0 for i in range(m)]
for i in range(1, n) : 
    for j in range(1, m) : 
        if C[i][0] == D[j][0] or C[i][1] == D[j][1] : 
            pref[i].append(j)
visit0 = [False for i in range(n)]
count = 0
for i in range(1, n) : 
    visit = visit0[:]
    if DFS(i) : 
        count = count + 1
print(count)