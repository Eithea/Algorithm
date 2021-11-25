import sys
input = sys.stdin.readline
from collections import deque

testcase = int(input())
for j in range(testcase) :        
    n = int(input())
    V = {}
    parent = [0 for i in range(n + 1)]
    for i in range(1, n + 1) : 
        V[i] = []
    l = list(map(int, input().split()))
    for i in range(n) : 
        V[l[i]] = l[i+1:]
        parent[l[i]] = i
    copy = parent[:]
    m = int(input())
    for i in range(m) : 
        v1, v2 = map(int, input().split())
        if copy[v2] < copy[v1] : 
            v1, v2 = v2, v1
        V[v2].append(v1)
        parent[v1] = parent[v1] + 1
        parent[v2] = parent[v2] - 1

    que = deque()
    for i in range(1, n + 1) : 
        if parent[i] == 0 : 
            que.append(i)
    if len(que) != 1 : 
        print("IMPOSSIBLE")
    ans = []
    while que : 
        now = que.popleft()
        ans.append(now)
        for next in V[now] : 
            parent[next] = parent[next] - 1
            if parent[next] == 0 : 
                que.append(next)
        if len(que) != 1 and len(ans) != n : 
            print("IMPOSSIBLE")
            break
    if len(ans) == n : 
        print(*ans)
