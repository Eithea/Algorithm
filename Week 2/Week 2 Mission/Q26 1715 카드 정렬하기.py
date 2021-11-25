import sys  
input = sys.stdin.readline
import heapq
n = int(input())
l = []
sum = 0
for i in range(n) : 
    c = int(input())
    heapq.heappush(l, c)

for i in range(n-1) : 
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    sum = sum + a + b
    heapq.heappush(l, a + b)
print(sum)