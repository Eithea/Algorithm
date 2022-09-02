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

N, k, D = map(int, input().split())
n = 1 + N + D + 1

maxF = [[0 for i in range(n)] for i in range(n)]
F = [[0 for i in range(n)] for i in range(n)]
connect = [[] for i in range(n)]

l = list(map(int, input().split()))
for i in range(D) : 
    connect[1+N+i].append(n-1)
    connect[n-1].append(1+N+i)
    maxF[1+N+i][n-1] = l[i]

for i in range(N) : 
    connect[0].append(1+i)
    connect[1+i].append(0)
    maxF[0][1+i] = k
    l = list(map(int, input().split()))
    for j in range(1, len(l)) : 
         connect[1+i].append(N+l[j])
         connect[N+l[j]].append(1+i)
         maxF[1+i][N+l[j]] = 1

print(flowBFS(0, n-1))