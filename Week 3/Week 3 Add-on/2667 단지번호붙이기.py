import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
T = []
gone = {}
for i in range(n) : 
    T.append(list(input()))
    for j in range(n) : 
        gone[(i, j)] = False
T.append([None for i in range(n + 1)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS(X, Y) : 
    que = deque()
    que.append([X, Y])
    gone[(X, Y)] = True
    count = 1
    while que : 
        a, b = que.popleft()
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if T[x][y] == '1' and not gone[(x, y)] : 
                gone[(x, y)] = True
                count = count + 1
                que.append([x, y])
    return count

ans = []
for i in range(n) : 
    for j in range(n) : 
        if T[i][j] == '1' and not gone[(i, j)] : 
            ans.append(BFS(i, j))
ans.sort()
print(len(ans))
for i in ans : 
    print(i)