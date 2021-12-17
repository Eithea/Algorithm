# base
import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase) : 
    break


# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# BFS
import sys
input = sys.stdin.readline
from collections import deque
# heap loop
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# defaultdict
import sys
input = sys.stdin.readline
from collections import defaultdict
V = defaultdict(int)

# input
n = int(input())
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n) : 
    l.append(list(input().split()))

