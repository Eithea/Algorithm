import sys  
input = sys.stdin.readline
import heapq
n = int(input())
ll = []
for i in range(n) : 
    a, b = map(int, input().split())
    ll.append([min(a, b), max(a, b)])
d = int(input())
l = []
for li in ll : 
    if li[1] - li[0] <= d : 
        l.append(li)
l.sort(key = lambda x : x[1])

heap = []
maxc = 0
for x in l : 
    if heap == [] : 
        heapq.heappush(heap, x)
    else : 
        while heap != [] and heap[0][0] < x[1] - d : 
            heapq.heappop(heap)
        heapq.heappush(heap, x)
    maxc = max(maxc, len(heap))
print(maxc)