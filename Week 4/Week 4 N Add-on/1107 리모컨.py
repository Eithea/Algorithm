import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict

n = int(input())
m = int(input())
l = list(map(int, input().split()))

V = defaultdict(int)
que = deque()
que.append([n, 0])
V[n] = 1
ans = sys.maxsize
while que : 
    x, k = que.popleft()
    if k >= ans : 
        continue
    if x == 100 : 
        ans = min(ans, k)
        break
    s= str(x)
    TF = True
    for i in range(m) : 
        if str(l[i]) in s : 
            TF = False
    if TF : 
        ans = min(ans, k + len(s))
    if V[x-1] == 0 : 
        V[x-1] = 1
        que.append([x-1, k+1])
    if V[x+1] == 0 : 
        V[x+1] = 1
        que.append([x+1, k+1])
print(ans)