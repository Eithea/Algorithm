import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
T = []
for i in range(n) : 
    T.append(list(map(int, input().split())))
DP = [[0 for i in range(m)] for i in range(n)]
# DP[i][j]는 [-1][-1]까지 갈 수 있는 경우의 수
gone = [[False for i in range(m)] for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(a, b) : 
    for i in range(4) : 
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and T[x][y] < T[a][b] : 
            if not gone[x][y] : 
                gone[x][y] = True
                DP[a][b] = DP[a][b] + DFS(x, y)
                # 현위치의 4방향에 대해 현위치보다 값이 낮다면 재귀
            else : 
                DP[a][b] = DP[a][b] + DP[x][y]
                # 이미 방문한(=DFS가 실행된) 위치라면 재귀하지 않고 DP값을 불러온다
    # 전위 재귀로 4방향에 대해 DP[a][b]를 갱신했으므로 이제 DP값이 있다
    return DP[a][b]
gone[0][0] = True
DP[-1][-1] = 1
print(DFS(0, 0))