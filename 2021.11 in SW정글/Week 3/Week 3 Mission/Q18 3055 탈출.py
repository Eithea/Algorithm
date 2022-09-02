import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
T = []
que = deque()
for i in range(r) : 
    T.append(list(input()))
    for j in range(c) : 
        if T[i][j] == '*' : 
            que.append([i, j, 0, '*'])
for i in range(r) : 
    for j in range(c) : 
        if T[i][j] == 'S' : 
            que.append([i, j, 0, 'S'])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que : 
    a, b, t, f = que.popleft()
    for i in range(4) : 
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < r and 0 <= y < c : 
            if f == '*' and (T[x][y] == '.' or T[x][y] == 'S') : 
                T[x][y] = f
                que.append([x, y, t + 1, f])
            elif f == 'S' and T[x][y] == '.' : 
                T[x][y] = f
                que.append([x, y, t + 1, f])
            elif f == 'S' and T[x][y] == 'D' : 
                print(t + 1)
                exit(0)
print('KAKTUS')