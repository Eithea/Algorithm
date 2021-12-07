import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
T = []
for i in range(n) : 
    T.append(list(map(int, input().split())))
DP = [[0 for i in range(m)] for i in range(n)]
gone = [[False for i in range(m)] for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(a, b) : 
    if DP[a][b] != 0 : 
        return DP[a][b] 
    for i in range(4) : 
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and T[x][y] < T[a][b] : 
            if not gone[x][y] : 
                gone[x][y] = True
                DP[a][b] = DP[a][b] + DFS(x, y)
            else : 
                DP[a][b] = DP[a][b] +DP[x][y]
    return DP[a][b]
gone[0][0] = True
DP[-1][-1] = 1
print(DFS(0, 0))