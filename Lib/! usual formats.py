# usual base
import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase) : 
    break

# usual input
n = int(input())
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n) : 
    l.append(list(input().split()))


# for DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# for BFS
import sys
input = sys.stdin.readline
from collections import deque

# for DIJK
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# for map
import sys
input = sys.stdin.readline
from collections import defaultdict
V = defaultdict(int)
