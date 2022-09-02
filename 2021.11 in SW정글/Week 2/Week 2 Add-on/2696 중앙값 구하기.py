import sys
input = sys.stdin.readline
import heapq
testcase = int(input())
for j in range(testcase) : 
    n = int(input())
    l = []
    if n % 10 == 0 : 
        for i in range(n // 10) : 
            l = l + list(map(int, input().split()))
    else : 
        for i in range(n // 10 + 1) : 
            l = l + list(map(int, input().split()))
    under = []
    over = []
    ans = []
    for i in range(n) : 
        x = l[i]
        if len(under) == len(over) : 
            heapq.heappush(under, -x)
        else : 
            heapq.heappush(over, x)
        if over != [] and -under[0] > over[0] : 
            a = -heapq.heappop(under)
            b = heapq.heappop(over)
            heapq.heappush(under, -b)
            heapq.heappush(over, a)
        if len(under) > len(over) : 
            ans.append(-under[0])
    s = len(ans)
    print(s)
    for i in range(s // 10) : 
        for k in range(9) : 
            print(ans[10 * i + k], end = ' ')
        print(ans[10 * i + 9])
    for k in range(s % 10 - 1) : 
        print(ans[s - s % 10 + k], end = ' ')
    print(ans[s-1])
