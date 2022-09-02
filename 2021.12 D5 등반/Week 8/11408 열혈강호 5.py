import sys
input = sys.stdin.readline
from collections import deque

def MCMF(start, end) : 
    mincost = 0
    maxflow = 0
    while True : 
        before = [-1 for i in range(left+right+2)]
        MC = [sys.maxsize for i in range(left+right+2)]
        inQ = [False for i in range(left+right+2)]
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
    return mincost, maxflow

left, right = map(int, input().split())

connect_source = [i for i in range(1, left+1)]
connect_left = [0] + [i for i in range(left+1, left+right+1)]
connect_right = [i for i in range(1, left+1)] + [left+right+1]
connect_sink = [i for i in range(left+1, left+right+1)]
connect = [connect_source] + [connect_left for j in range(left)] + [connect_right for j in range(right)] + [connect_sink]

maxF = [[0 for i in range(left+right+2)] for i in range(left+right+2)]
F = [[0 for i in range(left+right+2)] for i in range(left+right+2)]
C = [[0 for i in range(left+right+2)] for i in range(left+right+2)]

for i in range(1, right+1) : 
    maxF[left+i][left+right+1] = 1
for i in range(1, left+1) : 
    l = list(map(int, input().split()))
    maxF[0][i] = 1
    for x in range(l[0]) : 
        C[i][left+l[2*x+1]] = l[2*x+2]
        C[left+l[2*x+1]][i] = -l[2*x+2]
        maxF[i][left+l[2*x+1]] = 1

start, end = 0, left+right+1
mincost, maxflow = MCMF(start, end)
print(maxflow)
print(mincost)