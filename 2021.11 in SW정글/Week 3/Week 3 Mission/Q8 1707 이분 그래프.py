import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def DFS(v) : 
    global flag
    for next in V[v] : 
        if C[next] == 0 : 
            C[next] = - C[v] 
            DFS(next)
        elif C[next] == C[v] : 
            flag = False

k = int(input())
for i in range(k) : 
    Vn, En = map(int, input().split())
    V = [[] for i in range(Vn + 1)]
    C = [0 for i in range(Vn + 1)]
    for i in range(En) : 
        v1, v2 = map(int, input().split())
        V[v1].append(v2)
        V[v2].append(v1)

    flag = True
    i = 0
    while flag and i < Vn : 
        i = i + 1
        if C[i] == 0 : 
            C[i] = 1
            DFS(i)
    if flag : 
        print('YES')
    else : 
        print('NO')