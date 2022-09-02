import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
C = list(input().rstrip())
out = []
for i in range(n) : 
    C[i] = int(C[i])
    if C[i] == 0 : 
        out.append(i+1)

count = 0
V = [[] for i in range(n + 1)]
for i in range(n - 1) : 
    v1, v2 = map(int, input().split())
    if C[v1 - 1] + C[v2 - 1] == 2 : 
        count = count + 2
    else : 
        V[v1].append(v2)
        V[v2].append(v1)

sum = sum(C)
if sum == 0 : 
    print(0)
elif sum == 1 : 
    print(0)
elif sum == 2 : 
    print(2)
else : 
    def DFS(before, now) : 
        global ct
        if C[now - 1] == 1 : 
            ct = ct + 1
        else : 
            C[now - 1] = -1
            for next in V[now] : 
                if next != before : 
                    DFS(now, next)

    for i in out : 
        if C[i-1] == 0 : 
            ct = 0
            DFS(0, i)
            count = count + ct * (ct - 1)
    print(count)