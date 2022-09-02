import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if match[p] < 0 or DFS(match[p]) : 
            match[p] = now
            return True
    return False

from math import sqrt
def dis(X, Y) : 
    return sqrt((X[0] - Y[0])**2 + (X[1] - Y[1])**2)
while True : 
    try : 
        n, m, s, v = map(int, input().split())
        pref = [[] for i in range(n)]
        match = [-1 for i in range(m)]
        visit0 = [False for i in range(n)]
        nloc = [[] for i in range(n)]
        for i in range(n) : 
            nloc[i] = list(map(float, input().split()))

        for j in range(m) : 
            hole = list(map(float, input().split()))
            for i in range(n) : 
                if dis(nloc[i], hole) <= v * s + 0.00000001 : 
                    pref[i].append(j)

        count = 0
        for i in range(n) : 
            visit = visit0[:]
            if DFS(i) : 
                count = count + 1
        print(n - count)
    except : 
        break