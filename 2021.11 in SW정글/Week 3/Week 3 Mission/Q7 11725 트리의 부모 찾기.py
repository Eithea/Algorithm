import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
parent = [0 for i in range(n + 1)]
V = {}
for i in range(1, n + 1) : 
    V[i] = []
for i in range(n-1) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2)
    V[v2].append(v1)

def DFS(p) : 
    for i in V[p] : 
        if parent[i] == 0 : 
            parent[i] = p
            DFS(i)

DFS(1)
for i in range(2, n + 1) : 
    print(parent[i])