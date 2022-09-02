import sys
input = sys.stdin.readline
from collections import deque

n, m, h = map(int, input().split())
B = []
que = deque()
check = [[[False for i in range(n)] for j in range(m)] for k in range(h)]
for k in range(h) : 
    B.append([])
    for j in range(m) : 
        B[k].append(list(map(int, input().split())))
        for i in range(n) : 
            t = B[k][j][i]
            if t == 1 : 
                que.append([i, j, k])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while que : 
    a, b, c = que.popleft()
    for i in range(6) : 
        x = a + dx[i]
        y = b + dy[i]
        z = c + dz[i]
        if 0 <= x < n and 0 <= y < m and 0 <= z < h and B[z][y][x] == 0 and check[z][y][x] == False : 
            check[z][y][x] = True
            B[z][y][x] = B[c][b][a] + 1
            que.append([x, y, z])
f = True
date = 0
for k in range(h) : 
    for j in range(m) : 
        for i in range(n) : 
            if B[k][j][i] == 0 : 
                f = False
            date = max(date, B[k][j][i] - 1)
if f : 
    print(date)
else : 
    print(-1)