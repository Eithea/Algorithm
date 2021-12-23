# 행렬 제곱
n, b = map(int, input().split())
A = []
for i in range(n) : 
    A.append(list(map(int, input().split())))

I = [[0 for i in range(n)] for j in range(n)]
for i in range(n) : 
    I[i][i] = 1
    
for i in range(n) : 
    for j in range(n) : 
        A[i][j] = A[i][j] % 1000

def mult(A, B) : 
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            sum = 0
            for x in range(n) : 
                sum = sum + A[i][x] * B[x][j]
            C[i][j] = sum % 1000
    return C

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
for i in range(n) : 
    for j in range(n-1) :
        print(ans[i][j] , end = ' ')
    print(ans[i][-1])

