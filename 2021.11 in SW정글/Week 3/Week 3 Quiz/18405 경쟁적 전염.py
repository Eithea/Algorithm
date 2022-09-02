import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
T = []
V = [[] for i in range(k + 1)]
T.append([None for i in range(n + 1)])
for i in range(1, n + 1) : 
    T.append([None] + list(map(int, input().split())))
    for j in range(1, n + 1) : 
        if T[i][j] > 0 : 
            V[T[i][j]].append([i, j])
# 2차원 행렬 T를 인풋받은대로 만든다
# 좌표를 문제 조건과 맞추기 위해 0행과 0열은 비워둔다
# order i의 바이러스의 좌표를 V[i]에 담는다

s, X, Y = map(int, input().split())

que = deque()
for i in range(1, k + 1) : 
    for virus in V[i] : 
        que.append(virus)
que.append(['t', None])
# 큐를 만들고 바이러스를 order 순으로 큐에 넣는다
# 마지막으로 시간을 +1할 't'를 넣는다

t = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while que and t < s : 
    a, b = que.popleft()
    if a != 't' : 
        for i in range(4) : 
            x = a + dx[i]
            y = b + dy[i]
            if x <=n and y <= n and T[x][y] == 0 : 
                T[x][y] = T[a][b]
                que.append([x, y])
    # x, y가 0이라면 전염시키는 BFS
    # 큐에 order 순으로 들어갔으니 order가 작은 바이러스에 우선권이 있다
    else : 
        t = t + 1
        que.append(['t', None])
    # 시간 t에 대해 모든 바이러스가 일하고 나면 t+1하고 다시 반복한다
    # t가 s가 되면 while문 종료
print(T[X][Y])