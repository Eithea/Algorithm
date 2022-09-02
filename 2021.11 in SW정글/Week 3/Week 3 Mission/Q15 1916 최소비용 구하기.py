import sys
input = sys.stdin.readline
import heapq

Vn = int(input())
En = int(input())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2, c = map(int, input().split())
    V[v1].append([v2, c])
start, end = map(int, input().split())

maxc = 100000000
D = [maxc for i in range(Vn + 1)]

def DIJK(start) : 
    D[start] = 0
    heap = [[0, start]]
    while heap : 
        c, q = heapq.heappop(heap)
        if c <= D[q] : 
            for next in V[q] : 
                if c + next[1] < D[next[0]] : 
                    D[next[0]] = c + next[1]
                    heapq.heappush(heap, [c + next[1], next[0]])
DIJK(start)
print(D[end])