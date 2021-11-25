n = int(input())
W=[]
mincost = 0
for i in range(n) : 
    row = list(map(int, input().split()))
    W.append(row)
    mincost = mincost + sum(row)

def DFS(start, now, cost, gone) : 
    global mincost
    if len(gone) == n : 
        if W[now][start] != 0 : 
            mincost = min(mincost, cost + W[now][start])
        return
    for j in range(n) : 
        if cost + W[now][j] <= mincost : 
            if W[now][j] != 0 and j != start and j not in gone : 
                DFS(start, j, cost + W[now][j], gone + [j])

for i in range(n) : 
    DFS(i, i, 0, [i])
print(mincost)