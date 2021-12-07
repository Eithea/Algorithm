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
Vn, En = map(int, input().split())
l = list(map(int, input().split()))
for i in range(n) : 
    l.append(list(input().split()))

# graph dict
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v2].append(v1)

# topological sorting
parent = [0 for i in range(Vn + 1)]
parent[v1] = parent[v1] + 1
child = [0 for i in range(Vn + 1)]
child[v2] = child[v2] + 1