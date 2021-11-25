import sys
input = sys.stdin.readline
import heapq
under = []
over = []
n = int(input())
for i in range(n) : 
    x = int(input())
    if len(under) == len(over) : 
        heapq.heappush(under, -x)
    else : 
        heapq.heappush(over, x)
    if over != [] and -under[0] > over[0] : 
        a = -heapq.heappop(under)
        b = heapq.heappop(over)
        heapq.heappush(under, -b)
        heapq.heappush(over, a)
    print(-under[0])
