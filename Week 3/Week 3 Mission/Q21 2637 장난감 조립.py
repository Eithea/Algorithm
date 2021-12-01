import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
basic = [True for i in range(n + 1)]
parent = [0 for i in range(n)]
V = [[] for i in range(n + 1)]
for i in range(m) : 
    p, c, k = map(int, input().split())
    V[p].append([c, k])
    basic[p] = False
    parent[c] = parent[c] + 1

table = [0 for i in range(n)]
que = deque()
for i in range(1, n) : 
    if parent[i] == 0 : 
        que.append([i, 0])
que.append([n, 1])
while que : 
    c, k = que.popleft()
    for nextc, nextk in V[c] : 
        table[nextc] = table[nextc] + k * nextk
        parent[nextc] = parent[nextc] - 1
        if parent[nextc] == 0 : 
            que.append([nextc, table[nextc]])
for i in range(1, n) : 
    if basic[i] : 
        print(i, table[i])