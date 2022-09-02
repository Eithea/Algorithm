import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

Vn, En = map(int, input().split())
V = [[] for i in range(Vn + 1)]
U = [[] for i in range(Vn + 1)]
for i in range(En) : 
    big, small = map(int, input().split())
    V[big].append(small)
    U[small].append(big)

def DFS(dic, now) : 
    gone[now] = True
    for next in dic[now] : 
        if not gone[next] : 
            DFS(dic, next)
            
count = 0
for i in range(1, Vn + 1) : 
    gone = [False for i in range(Vn + 1)]
    DFS(V, i)
    if sum(gone) - 1 >= Vn // 2 + 1 : 
        count = count + 1
    else : 
        gone = [False for i in range(Vn + 1)]
        DFS(U, i)
        if sum(gone) - 1 >= Vn // 2 + 1 : 
            count = count + 1
print(count)
