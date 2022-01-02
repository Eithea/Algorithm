import sys
input = sys.stdin.readline
from collections import deque

def MCMF(start, end) : 
    mincost = 0
    maxflow = 0
    i = 2
    while i : 
        before = [-1 for i in range(2*n)]
        MC = [sys.maxsize for i in range(2*n)]
        inQ = [False for i in range(2*n)]
        que = deque()
        que.append(start)
        MC[start] = 0
        inQ[start] = True
        while que : 
            now = que.popleft()
            inQ[now] = False
            for next in connect[now] : 
                if maxF[now][next] - F[now][next] > 0 and MC[next] > MC[now] + C[now][next] : 
                    MC[next] = MC[now] + C[now][next]
                    before[next] = now
                    if not inQ[next] : 
                        que.append(next)
                        inQ[next] = True
        if before[end] == -1 : 
            break
        now = end
        while now != start : 
            mincost = mincost + C[before[now]][now]
            F[before[now]][now] = F[before[now]][now] + 1
            F[now][before[now]] = F[now][before[now]] - 1
            now = before[now]
        maxflow = maxflow + 1
        i = i - 1
    return mincost, maxflow


while True : 
    try : 
        n, m = map(int, input().split())

        maxF = [[0 for i in range(2*n)] for i in range(2*n)]
        F = [[0 for i in range(2*n)] for i in range(2*n)]
        connect = [[] for i in range(2*n)]
        C = [[0 for i in range(2*n)] for i in range(2*n)]

        for v in range(n) : 
            connect[2*v].append(2*v+1)
            connect[2*v+1].append(2*v)
            maxF[2*v][2*v+1] = 1

        for i in range(m) : 
            v1, v2, c = map(int, input().split())
            v1 = v1 - 1
            v2 = v2 - 1
            connect[2*v1+1].append(2*v2)
            connect[2*v2].append(2*v1+1)
            maxF[2*v1+1][2*v2] = 1
            C[2*v1+1][2*v2] = c
            C[2*v2][2*v1+1] = -c

        start = 0
        end = n-1
        mincost, maxflow = MCMF(2*start+1, 2*end)
        print(mincost)
    except : 
        break