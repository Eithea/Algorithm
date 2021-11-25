import sys
input = sys.stdin.readline
from heapq import heappush, heappop

Vn, En = map(int, input().split())
V = {}
parent = [0 for i in range(Vn + 1)]
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    parent[v2] = parent[v2] + 1

heap = []
for i in range(1, Vn + 1) : 
    if parent[i] == 0 : 
        heappush(heap, i)

while heap : 
    i = heappop(heap)
    print(i, end = ' ')
    for j in V[i] : 
        parent[j] = parent[j] - 1
        if parent[j] == 0 : 
            heappush(heap, j)
