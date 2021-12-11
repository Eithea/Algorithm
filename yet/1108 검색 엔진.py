import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
IP = []
for i in range(n) : 
    IP.append(list(input().split()))

site = set([])
V = {}
rV = {}
parent = {}
value = {}
for i in range(n) : 
    v1 = IP[i][0]
    v2s = IP[i][2:]
    site.add(v1)
    rV[v1] = v2s
    parent[v1] = len(v2s)
    value[v1] = 1
    for j in v2s : 
        try : 
            V[j].append(v1)
        except : 
            site.add(j)
            V[j] = []
            V[j].append(v1)
test = True
for s in site : 
    try : 
        test = parent[s]
    except : 
        parent[s] = 0
        value[s] = 1
trg = input().rstrip()

print(site, V, rV, parent, value, sep = '\n')
que = deque()
for s in site : 
    if parent[s] == 0 : 
        que.append(s)
while que : 
    now = que.popleft()
    try : 
        for next in V[now] : 
                parent[next] = parent[next] - 1
                if parent[next] == 0 : 
                    que.append(next)
    except : 
        pass
    try : 
        sum = 0
        for before in rV[now] : 
            sum = sum + value[before]
    except : 
        sum = 0
    value[now] = value[now] + sum
print(value[trg])