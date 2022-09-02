import sys  
input = sys.stdin.readline
import heapq
l = []
xpick= {0}
n = int(input())
for i in range(n) : 
    elem = list(map(int, input().split()))
    l.append(elem)
    xpick.add(elem[0])
    xpick.add(elem[2])
l.sort(key=lambda x : (x[0], -x[1]))
xpick = sorted(list(xpick))
del xpick[0]
i = 0
heap = []
for now in xpick : 
    while i < n and l[i][0] == now : 
        if heap == [] : 
            print(l[i][0], end = ' ')
            print(l[i][1], end = ' ')
        elif l[i][1] > -heap[0][0] : 
            print(l[i][0], end = ' ')
            print(l[i][1], end = ' ')
        heapq.heappush(heap, [-l[i][1], l[i][2]])
        i = i + 1
    if heap != [] and now == heap[0][1] : 
        high = heapq.heappop(heap)
        while heap != [] and now >= heap[0][1] : 
            heapq.heappop(heap)
        if heap == [] : 
            print(high[1], end = ' ')
            print(0, end = ' ')
        elif high[0] != heap[0][0] : 
            print(high[1], end = ' ')
            print(-heap[0][0], end = ' ')