import sys
input = sys.stdin.readline
from collections import deque

Vn, En = map(int, input().split())

V = {}
upper = 1
lower = 1000000000
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2, c = map(int, input().split())
    V[v1].append([v2, c])
    V[v2].append([v1, c])
    upper = max(upper, c)
    lower = min(lower, c)
start, end = map(int, input().split())

def BFS(weight) : 
    que = deque()
    que.append(start)
    gone[start] = True
    while que : 
        now = que.popleft()
        if now == end : 
            return True
        for next, limit in V[now] : 
            if not gone[next] and limit >= weight : 
                gone[next] = True
                que.append(next)
    return False

while upper >= lower : 
    gone = [False for i in range(Vn + 1)]
    center = (upper + lower) // 2
    if BFS(center) : 
        lower = center + 1
    else : 
        upper = center - 1
print(upper)
