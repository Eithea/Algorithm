import sys
input = sys.stdin.readline
from collections import deque
from collections import defaultdict

def TRkey(x) : 
    n = ord(x) - 97
    return 1<<n
def TRdoor(x) : 
    n = ord(x) - 65
    return 1<<n
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS() : 
    global count, key, door
    while que : 
        a, b = que.popleft()
        f = T[a][b]
        if 96 < ord(f) < 123 : 
            key = key | TRkey(f)
        elif 64 < ord(f) < 91 : 
            if not open[(a, b)] : 
                D.append([f, a, b])
                continue
        elif f == '$' : 
            count = count + 1
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and T[x][y] != '*' and not gone[(x, y)] : 
                gone[(x, y)] = 1
                que.append([x, y])
testcase = int(input())
for t in range(testcase) : 
    key = 0
    D = []
    gone = defaultdict(int)
    open = defaultdict(int)
    count = 0

    n, m = map(int, input().split())
    T = []
    for i in range(n) : 
        T.append(list(input().rstrip()))

    l = input().rstrip()
    if l != '0' : 
        for i in range(len(l)) : 
            key = key | TRkey(l[i])


    que = deque()

    for i in range(n) : 
        if T[i][0] != '*' and not gone[(i, 0)] : 
            gone[(i, 0)] = 1
            que.append([i, 0])
            BFS()
        if T[i][m-1] != '*' and not gone[(i, m-1)] : 
            gone[(i, m-1)] = 1
            que.append([i, m-1])
            BFS()
    for j in range(m) : 
        if T[0][j] != '*' and not gone[(0, j)] : 
            gone[(0, j)] = 1
            que.append([0, j])
            BFS()
        if T[n-1][j] != '*' and not gone[(n-1, j)] : 
            gone[(n-1, j)] = 1
            que.append([n-1, j])
            BFS()

    for door, i, j in D : 
        if key & TRdoor(door) : 
            open[(i, j)] = 1
            que.append([i, j])
    while que : 
        BFS()
        for door, i, j in D : 
            if not open[(i, j)] and key & TRdoor(door) : 
                open[(i, j)] = 1
                que.append([i, j])
    print(count)