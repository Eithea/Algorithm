import sys
input = sys.stdin.readline

Vn, En = map(int, input().split())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    V[v2].append(v1)

gone = []
count = 0
def BFS(now) : 
    que = [now]
    while que : 
        q = que[0]
        gone.append(q)
        del que[0]
        for i in V[q] : 
            if not i in gone and not i in que : 
                que.append(i)
for i in range(1, Vn + 1) : 
    if not i in gone : 
        count = count + 1
        BFS(i)
print(count)