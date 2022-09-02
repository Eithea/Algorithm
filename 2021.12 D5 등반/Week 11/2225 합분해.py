p = 1000000000
f = [[0 for i in range(201)] for i in range(201)]
for i in range(201) : 
    f[i][0] = 1

for i in range(1, 201) : 
    for j in range(1, 201) : 
        f[i][j] = (f[i-1][j] + f[i][j-1]) %p

n, k = map(int, input().split())
print(f[k][n])