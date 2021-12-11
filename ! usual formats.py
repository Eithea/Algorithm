# base
import sys
input = sys.stdin.readline

testcase = int(input())
for t in range(testcase) : 
    break


# DFS
sys.setrecursionlimit(10**8)
# BFS
from collections import deque
# heap loop
from heapq import heappush, heappop

# defaultdict
from collections import defaultdict
V = defaultdict(int)

# input
n = int(input())
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n) : 
    l.append(list(input().split()))

