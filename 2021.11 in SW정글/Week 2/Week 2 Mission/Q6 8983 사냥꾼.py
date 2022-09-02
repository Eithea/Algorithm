import sys  
input = sys.stdin.readline
from bisect import bisect_left

m, n, l = map(int, input().split())
line = list(map(int, input().split()))

line.sort()
count = 0
for i in range(n) : 
    x, y = map(int, input().split())
    if not y > l : 
        if x <= line[0] : 
            if line[0] - x <= l - y : 
                count = count + 1
        elif x >= line[-1] : 
            if x - line[-1] <= l - y : 
                count = count + 1
        else :     
            a = bisect_left(line, x)
            if min(x - line[a-1], line[a] - x) <= l - y : 
                count = count + 1
print(count)