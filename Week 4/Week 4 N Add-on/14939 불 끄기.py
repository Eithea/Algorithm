V = []
n = 10
for i in range(n) : 
    V.append(list(input()))
    for j in range(n) : 
        if V[i][j] == 'O' : 
            V[i][j] = 1
        else : 
            V[i][j] = 0

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
def push(a, b) : 
    global count
    count = count + 1
    for i in range(5) : 
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < n : 
            U[x][y] = abs(U[x][y] - 1)

minc = n ** 2 + 1
for bit in range(1<<n) : 
    U = [V[i][:] for i in range(n)]
    count = 0
    for j in range(n) : 
        if bit & (1<<j) : 
            push(0, j)
    for i in range(1, n) : 
        for j in range(n) : 
            if U[i-1][j] == 1 : 
                push(i, j)
    if max(U[-1]) == 0 : 
        minc = min(minc, count)
if minc == n ** 2 + 1 :
    print(-1)
else : print(minc)