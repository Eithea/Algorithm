import sys
input = sys.stdin.readline
import heapq

V = []
n= int(input())
for i in range(n) : 
    V.append(list(input()))

def cost(x) : 
    if x == '1' : 
        return 0
    if x == '0' : 
        return 1

maxc = 2 * n
D = {}
for i in range(n) : 
    for j in range(n) : 
        D[(i, j)] = maxc

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DIJK(start) : 
    D[start] = 0
    heap = [[0, start]]
    while heap : 
        c, q = heapq.heappop(heap)
        if c <= D[q] : 
            for i in range(4) : 
                x = q[0] + dx[i]
                y = q[1] + dy[i]
                if x < 0 or y < 0 or x >= n or y >= n : 
                    continue
                if c + cost(V[x][y]) < D[(x, y)] : 
                    D[(x, y)] = c + cost(V[x][y])
                    heapq.heappush(heap, [c + cost(V[x][y]), (x, y)])
DIJK((0, 0))
print(D[(n-1, n-1)])