import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
T = []
for i in range(n) : 
    T.append(list(input()))
T.append([None for i in range(n + 1)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS(X, Y) : 
    color = T[X][Y]
    que = deque()
    que.append([X, Y])
    gone[(X, Y)] = True
    while que : 
        a, b = que.popleft()
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if T[x][y] == color and not gone[(x, y)] : 
                gone[(x, y)] = True
                que.append([x, y])
def BFSrg(X, Y) : 
    color = T[X][Y]
    rg = False
    if color == 'R' or color == 'G' : 
        rg = True
    que = deque()
    que.append([X, Y])
    gone[(X, Y)] = True
    while que : 
        a, b = que.popleft()
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if T[x][y] == color or rg and T[x][y] == 'R' or rg and T[x][y] == 'G' : 
                if not gone[(x, y)] : 
                    gone[(x, y)] = True
                    que.append([x, y])

count = 0
gone = {}
for i in range(n) :
    for j in range(n) : 
        gone[(i, j)] = False
for i in range(n) : 
    for j in range(n) : 
        if not gone[(i, j)] : 
            BFS(i, j)
            count = count + 1
print(count, end = ' ')
count = 0
for i in range(n) :
    for j in range(n) : 
        gone[(i, j)] = False
for i in range(n) : 
    for j in range(n) : 
        if not gone[(i, j)] : 
            BFSrg(i, j)
            count = count + 1
print(count)