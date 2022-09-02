import sys  
input = sys.stdin.readline
import heapq
l = []
n = int(input())
for i in range(n) : 
    elem = list(map(int, input().split()))
    l.append(elem)
l.append([0, 0, 1000000002])
l.append([1000000001, 0, 1000000002])
l.sort(key=lambda x : (x[0], -x[1]))

heap = [[0, 0, 1000000002]]
for a, h, b in l : 
    if a == 0 : 
        continue
    else : 
        trash = []
        hnow = 0
        while heap[0][2] <= a : 
            t = heapq.heappop(heap)
            heapq.heappush(trash, [t[2], -t[0]])
        if trash != [] : 
            stack = []
            for i in range(len(trash)) : 
                high = heapq.heappop(trash)
                while stack != [] and stack[-1][1] <= high[1] : 
                    del stack[-1]
                stack.append(high)
                
            for i in range(len(stack) - 1) : 
                print(stack[i][0], stack[i+1][1], end = ' ')
            if stack[-1][0] == a : 
                hnow = stack[-1][1]
                if hnow > h : 
                    print(stack[-1][0], h, end = ' ')
            else : 
                print(stack[-1][0], -heap[0][0], end = ' ')

        if h > -heap[0][0] and h > hnow : 
            print(a, h, end = ' ')
        heapq.heappush(heap, [-h, a, b])