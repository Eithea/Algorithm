import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
T = []
for i in range(n) : 
    T.append(list(map(int, input().split())))

def Bcheck(Blist, i, j) : 
    diff = i - j
    for x, y in Blist : 
        if x - y == diff : 
            return False
    return True

def DFS(Blist, level) : 
    global maxB
    if n  - level//2 + len(Blist) < maxB : 
        return
    if level >= 2 * n - 1 : 
        maxB = max(maxB, len(Blist))
        return
    for i in range(level + 1) : 
        j = level - i
        if i < n and j < n and T[i][j] == 1 and Bcheck(Blist, i, j) : 
            DFS(Blist + [[i, j]], level + 2)
    DFS(Blist, level + 2)

maxB = 0
DFS([], 0)
Bodd = maxB

maxB = 0
DFS([], -1)
Beven = maxB

print(Bodd + Beven)