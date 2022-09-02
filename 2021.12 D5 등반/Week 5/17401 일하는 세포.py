import sys
input = sys.stdin.readline

p = 1000000007
def mult(A, B) : 
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            sum = 0
            for x in range(n) : 
                sum = sum + A[i][x] * B[x][j]
            C[i][j] = sum % p
    return C

t, n, d = map(int, input().split())
b = d // t
r = d % t
maped = [[[0 for i in range(n)] for i in range(n)] for i in range(t)]
for tt in range(t) : 
    x = int(input())
    for xx in range(x) : 
        i, j, w = map(int, input().split())
        maped[tt][i-1][j-1] = w


A = [maped[0][i][:] for i in range(n)]
for i in range(1, t) : 
    A = mult(A, maped[i])

I = [[0 for i in range(n)] for j in range(n)]
for i in range(n) : 
    I[i][i] = 1

powerlist = [0 for i in range(37)]
powerlist[0] = A
for i in range(1, 37) : 
    powerlist[i] = mult(powerlist[i-1], powerlist[i-1])

bilist = [0 for i in range(37)]
for i in range(36, -1, -1) : 
    bilist[i] = b // pow(2, i)
    b = b - bilist[i] * pow(2, i)

ans = [[] for i in range(n)]
if bilist[0] == 1 : 
    for i in range(n) : 
        ans[i] = powerlist[0][i][:]
else : 
    for i in range(n) : 
        ans[i] = I[i][:]
for i in range(1, 37) : 
    if bilist[i] == 1 : 
        ans = mult(ans, powerlist[i])

for i in range(r) : 
    ans = mult(ans, maped[i])

for i in range(n) : 
    print(*ans[i])