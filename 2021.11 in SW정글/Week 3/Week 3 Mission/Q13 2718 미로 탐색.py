import sys
input = sys.stdin.readline
n, m = map(int, input().split())

T = []
for i in range(n) :
    T.append(list(input()))
T.append([None for i in range(m+1)])

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
            if T[x][y] == '1' : 
                T[x][y] = T[a][b] + 1
                que.append([x, y])
            elif type(T[x][y]) is int and T[a][b] + 1 < T[x][y] : 
                T[x][y] = T[a][b] + 1
                que.append([x, y])
T[0][0] = 1
BFS(0, 0)
print(T[n-1][m-1])