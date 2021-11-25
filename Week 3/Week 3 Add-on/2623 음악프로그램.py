import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
V = {}
parent = [0 for i in range(n + 1)]
for i in range(1, n + 1) : 
    V[i] = []
for i in range(m) : 
    l = list(map(int, input().split()))
    for i in range(1, l[0]) : 
        V[l[i]].append(l[i+1])
        parent[l[i+1]] = parent[l[i+1]] + 1

que = deque()
for i in range(1, n + 1) : 
    if parent[i] == 0 : 
        que.append(i)
ans = []
while que : 
    i = que.popleft()
    ans.append(i)
    for j in V[i] : 
        parent[j] = parent[j] - 1
        if parent[j] == 0 : 
            que.append(j)

if len(ans) == n : 
    for i in ans : 
        print(i)
else : 
    print(0)