import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
V = []
for i in range(n) : 
    V.append(list(map(int, input().split())))

max = sys.maxsize
DP = [[max for i in range(1<<n)] for i in range(n)]

def D(v1, v2) : 
    d = ((v1[0]-v2[0]) ** 2 + (v1[1]-v2[1]) ** 2) ** 0.5
    return d

def DFS(start, now, gone) :
    if DP[now][gone] != max : 
        return DP[now][gone]     
    if gone == (1<<n) - 1 : 
        DP[now][gone] = D(V[now], V[start])
        return DP[now][gone]
    for next in range(n) : 
        if not gone & 1<<next : 
            DP[now][gone] = min(DP[now][gone], DFS(start, next, gone | 1<<next) + D(V[now], V[next]))
    return DP[now][gone]

print(DFS(0, 0, 1))