import sys
input = sys.stdin.readline

Vn, En, v = map(int, input().split())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    V[v2].append(v1)
for i in range(1, Vn + 1) : 
    V[i].sort()

gone = []
def DFS(now) : 
    print(now, end = ' ')
    gone.append(now)
    for i in V[now] : 
        if not i in gone : 
            DFS(i)
DFS(v)
print()

gone = []
def BFS(now) : 
    que = [now]
    while que : 
        q = que[0]
        print(q, end = ' ')
        gone.append(q)
        del que[0]
        for i in V[q] : 
            if not i in gone and not i in que : 
                que.append(i)
BFS(v)