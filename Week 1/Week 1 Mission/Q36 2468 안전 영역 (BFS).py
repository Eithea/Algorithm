import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
maxheight = 0
minheight = 101
n = int(input())
originH = []
for i in range(n) : 
    row = list(map(int, input().split()))
    maxheight = max(maxheight, max(row))
    minheight = min(minheight, min(row))
    originH.append(row)

# n = 5
# originH = [[6,8,2,6,2],[3,2,3,4,6],[6,7,3,3,2],[7,2,5,3,6],[8,9,5,2,7]]
# minheight = 2
# maxheight = 9

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS(X, Y) : 
    que = [[X, Y]]
    while que : 
        a, b = que[0][0], que[0][1]
        del que[0]
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if footprint[x][y] > 0 : 
                footprint[x][y] = 0
                que.append([x, y])

H = [[0]*(n+2)]*(n+2)
maxc = 0
for i in range(n) : 
    H[i+1] = [0] + originH[i] + [0]

for h in range(minheight - 1, maxheight) : 
    footprint = [[1]*(n+2) for i in range(n+2)]
    count = 0
    for i in range(n+2) : 
        for j in range(n+2) : 
            if H[i][j] <= h : 
                footprint[i][j] = 0
    for i in range(n+2) : 
        for j in range(n+2) : 
            if footprint[i][j] == 1 : 
                footprint[i][j] = 0
                BFS(i, j)
                count = count + 1
    maxc = max(maxc, count)
print(maxc)
    