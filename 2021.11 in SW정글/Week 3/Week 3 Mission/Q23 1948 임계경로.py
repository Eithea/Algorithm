import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

Vn = int(input())
En = int(input())
V = {}
child = [0 for i in range(Vn + 1)]
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2, c = map(int, input().split())
    V[v1].append([v2, c])
    child[v1] = child[v1] + 1
start, end = map(int, input().split())

D = [0 for i in range(Vn + 1)]
def DFS1(now) : 
    for next, cost in V[now] : 
        if child[next] == 0 : 
            child[now] = child[now] - 1
            D[now] = max(D[now], D[next] + cost)
        else : 
            child[now] = child[now] - 1
            DFS1(next)
    for next, cost in V[now] : 
        D[now] = max(D[now], D[next] + cost)
DFS1(start)
print(D[start])

gone = [False for i in range(Vn + 1)]
count = 0
def DFS2(now) : 
    global count
    for next, cost in V[now] : 
        if D[now]- D[next] == cost : 
            count = count + 1
            if not gone[next] : 
                gone[next] = True
                DFS2(next)
DFS2(start)
print(count)