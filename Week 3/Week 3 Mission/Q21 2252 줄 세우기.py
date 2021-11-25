import sys
input = sys.stdin.readline
from collections import deque

Vn, En = map(int, input().split())
parent = [0 for i in range(Vn + 1)]
V = [[] for i in range(Vn + 1)]
for i in range(En) : 
    big, small = map(int, input().split())
    V[big].append(small)
    parent[small] = parent[small] + 1

que = deque()
for i in range(1, Vn + 1) : 
    if parent[i] == 0 : 
        que.append(i)

while que : 
    now = que.popleft()
    print(now, end = ' ')
    for next in V[now] : 
        parent[next] = parent[next] - 1
        if parent[next] == 0 : 
            que.append(next)