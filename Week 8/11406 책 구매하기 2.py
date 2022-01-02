import sys
input = sys.stdin.readline
from collections import deque

def flowBFS(start, end) : 
    maxflow = 0
    while True : 
        before = [-1 for i in range(m+n+2)]
        que = deque()
        que.append(start)
        while que : 
            now = que.popleft()
            for next in connect[now] : 
                if maxF[now][next] - F[now][next] > 0 and before[next] == - 1 : 
                    que.append(next)
                    before[next] = now
                    if next == end : 
                        break
        if before[end] == -1 : 
            break
        flow = sys.maxsize
        now = end
        while now != start : 
            flow = min(flow, maxF[before[now]][now] - F[before[now]][now])
            now = before[now]
        now = end
        while now != start : 
            F[before[now]][now] = F[before[now]][now] + flow
            F[now][before[now]] = F[now][before[now]] - flow
            now = before[now]
        maxflow = maxflow + flow
    return maxflow

n, m = map(int, input().split())

connect_source = [i for i in range(1, m+1)]
connect_left = [0] + [i for i in range(m+1, m+n+1)]
connect_right = [i for i in range(1, m+1)] + [m+n+1]
connect_sink = [i for i in range(m+1, m+n+1)]
connect = [connect_source] + [connect_left for j in range(m)] + [connect_right for j in range(n)] + [connect_sink]

maxF = [[0 for i in range(m+n+2)] for i in range(m+n+2)]
F = [[0 for i in range(m+n+2)] for i in range(m+n+2)]
ln = list(map(int, input().split()))
for i in range(1, n+1) : 
    maxF[m+i][m+n+1] = ln[i-1]
lm = list(map(int, input().split()))
for i in range(1, m+1) : 
    maxF[0][i] = lm[i-1]

for i in range(1, m+1) : 
    lc = list(map(int, input().split()))
    for j in range(m+1, m+n+1) : 
        maxF[i][j] = lc[j-m-1]

start, end = 0, m+n+1
maxflow = flowBFS(start, end)
print(maxflow)