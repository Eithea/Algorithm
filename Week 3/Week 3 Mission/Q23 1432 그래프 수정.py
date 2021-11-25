import sys
input = sys.stdin.readline
import heapq

n = int(input())
child = [0 for i in range(n + 1)]
V = [[] for i in range(n + 1)]
for i in range(1, n + 1) : 
    l = list(input())
    for j in range(1, n + 1) : 
        if l[j-1] == '1' : 
            V[j].append(i)
            child[i] = child[i] + 1

child[0] = None
if 0 not in child : 
    print(-1)
    exit(0)

heap = []
for i in range(1, n + 1) : 
    if child[i] == 0 : 
        heapq.heappush(heap, -i)
ans = [0 for i in range(n + 1)]
order = n
while heap : 
    i = -heapq.heappop(heap)
    ans[i] = order
    order = order - 1
    for j in V[i] : 
        child[j] = child[j] - 1
        if child[j] == 0 : 
            heapq.heappush(heap, -j)

for i in range(1, n + 1) : 
    print(ans[i], end = ' ')