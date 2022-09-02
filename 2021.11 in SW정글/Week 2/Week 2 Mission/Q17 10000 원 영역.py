import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from bisect import bisect_left

n = int(input())
l = []
for i in range(n) : 
    x, r = map(int, input().split())
    l.append([x - r, x + r])
l.sort(key = lambda x : (x[0], -x[1]))

count = 0
def check(big, small) : 
    global count
    if big[1] == small[1] : 
        count = count + 1
        return
    nextidx = bisect_left(l, [small[1], -1000000000])
    if nextidx == len(l) : 
        return
    if small[1] == l[nextidx][0] : 
        check(big, l[nextidx])

for i in range(n-1) : 
    if l[i][0] == l[i+1][0] : 
        check(l[i], l[i+1])
print(1 + n + count)