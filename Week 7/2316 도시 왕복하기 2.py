import sys
input = sys.stdin.readline
from collections import deque

def flowBFS(start, end) : 
    flowsum = 0
    while True : 
        before = [-1 for i in range(n)]
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
        flowsum = flowsum + flow
    return flowsum

n, m = map(int, input().split())

n = (n + 1) * 2
maxF = [[0 for i in range(n)] for i in range(n)]
F = [[0 for i in range(n)] for i in range(n)]
connect = [[] for i in range(n)]

for i in range(m) : 
    v1, v2 = map(int, input().split())
    connect[v1].append(v2 + n//2)
    connect[v1 + n//2].append(v2)
    connect[v2].append(v1 + n//2)
    connect[v2 + n//2].append(v1)
    maxF[v1 + n//2][v2] = maxF[v1 + n//2][v2] + 1
    maxF[v2 + n//2][v1] = maxF[v2 + n//2][v1] + 1


for v in range(n//2) : 
    connect[v].append(v + n//2)
    connect[v + n//2].append(v)
    maxF[v][v + n//2] = maxF[v][v + n//2] + 1

print(flowBFS(1 + n//2, 2))