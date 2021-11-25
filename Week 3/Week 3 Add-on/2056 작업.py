import sys
input = sys.stdin.readline
from collections import deque

Vn = int(input())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
B = [0 for i in range(Vn + 1)]
parent = [0 for i in range(Vn + 1)]
for i in range(1, Vn + 1) : 
    l = list(map(int, input().split()))
    B[i] = l[0]
    for j in range(2, len(l)) : 
        V[l[j]].append(i)
    parent[i] = parent[i] + len(l) - 2

que = deque()
for i in range(1, Vn + 1) : 
    if parent[i] == 0 : 
        que.append(i)

D = B[:]
while que : 
    now = que.popleft()
    for next in V[now] : 
        D[next] = max(D[next], D[now] + B[next])
        parent[next] = parent[next] - 1
        if parent[next] == 0 : 
            que.append(next)
print(max(D))