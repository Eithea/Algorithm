import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
T = []
que = deque()
for i in range(n) : 
    T.append(list(map(int, input().split())) + [None])
    for j in range(m) : 
        if T[i][j] != 0 : 
            que.append([i, j])
T.append([None for i in range(m + 1)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def cutcheck(ice) : 
    gone = {}
    for a, b in ice : 
        gone[(a, b)] = False
    a, b = ice[0][0], ice[0][1]
    gone[(a, b)] = True
    q = deque()
    q.append([a, b])
    check = 1
    while q : 
        a, b = q.popleft()
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if T[x][y] > 0 and not gone[(x, y)] : 
                gone[(x, y)] = True
                q.append([x, y])
                check = check + 1
    if check != len(ice) : 
        return True
    return False

year = -1
que.append(['year', year - 1])
while que : 
    a, b = que.popleft()
    if a != 'year' : 
        count = 0
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            #  year == T[x][y]이면 올해 녹은 바다이니 count하면 안됨
            if year < T[x][y] <= 0 : 
                count = count + 1
        if T[a][b] > count : 
            que.append([a, b])
            T[a][b] = T[a][b] - count
        else : 
            T[a][b] = year
    else : 
        if len(que) == 0 : 
            print(0)
            exit(0)
        else : 
            if cutcheck(que) : 
                print(-year)
                exit(0)
            else : 
                year = b
                que.append(['year', b - 1])
