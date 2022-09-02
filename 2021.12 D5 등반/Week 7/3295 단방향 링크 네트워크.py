import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if match[p] == -1 or DFS(match[p]) : 
            match[p] = now
            return True
    return False

testcase = int(input())
for t in range(testcase) : 
    n, m = map(int, input().split())
    pref = [[] for i in range(n)]
    match = [-1 for i in range(n)]
    visit0 = [False for i in range(n)]

    for i in range(m) : 
        u, v = map(int, input().split())
        pref[u].append(v)

    count = 0
    for i in range(n) : 
        visit = visit0[:]
        if DFS(i) : 
            count = count + 1
    print(count)