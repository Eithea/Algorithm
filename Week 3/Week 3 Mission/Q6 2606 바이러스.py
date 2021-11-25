import sys
input = sys.stdin.readline

Vn = int(input())
En = int(input())
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
count = 0
def BFS(now) : 
    global count
    que = [now]
    while que : 
        q = que[0]
        gone.append(q)
        del que[0]
        for i in V[q] : 
            if not i in gone and not i in que : 
                que.append(i)
                count = count + 1
BFS(1)
print(count)