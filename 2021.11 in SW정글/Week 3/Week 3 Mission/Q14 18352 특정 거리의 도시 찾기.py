import sys
input = sys.stdin.readline

Vn, En, k, x = map(int, input().split())

V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)

gone = [False for i in range(Vn+1)]
ans = []
def BFS(now) : 
    que = [[now, 0]]
    while que : 
        q, d = que[0][0], que[0][1]
        del que[0]
        if d == k : 
            ans.append(q)
        else : 
            for i in V[q] : 
                if not gone[i] : 
                    gone[i] =True
                    que.append([i, d + 1])
gone[x] = True
BFS(x)
if ans == [] : 
    print(-1)
else : 
    ans.sort()
    for i in ans : 
        print(i)