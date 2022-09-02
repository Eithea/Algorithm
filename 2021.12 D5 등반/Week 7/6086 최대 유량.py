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

n = 58

maxF = [[0 for i in range(n)] for i in range(n)]
F = [[0 for i in range(n)] for i in range(n)]
connect = [[] for i in range(n)]

m = int(input())
for i in range(m) : 
    v1, v2, f = input().split()
    v1 = ord(v1) - 65
    v2 = ord(v2) - 65
    f = int(f)
    connect[v1].append(v2)
    connect[v2].append(v1)
    maxF[v1][v2] = maxF[v1][v2] + f
    maxF[v2][v1] = maxF[v2][v1] + f
print(flowBFS(0, 25))