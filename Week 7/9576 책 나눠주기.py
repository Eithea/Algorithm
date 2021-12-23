import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def countnon0(match) : 
    count = 0
    for i in match : 
        if i : 
            count = count + 1
    return count

def DFS(now) : 
    if visit[now] : 
        return False
    visit[now] = True
    for p in pref[now] : 
        if not match[p] or DFS(match[p]) : 
            match[p] = now
            return True
    return False

testcase = int(input())
for t in range(testcase) : 
    m, n = map(int, input().split())
    pref = [[] for i in range(n+1)]
    match = [0 for i in range(m+1)]
    visit0 = [0 for i in range(n+1)]

    for i in range(1, n+1) : 
        a, b = map(int, input().split())
        for p in range(a, b+1) : 
            pref[i].append(p)
    for i in range(1, n+1) : 
        visit = visit0[:]
        DFS(i)

    print(countnon0(match))