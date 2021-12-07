# 에라토스테네스의 체
n = 10000000
eratos = [1 for i in range(n + 1)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(n ** 0.5) + 2) : 
    if eratos[i] == 1 : 
        for j in range(2 * i, n + 1, i) : 
            eratos[j] = 0

# 팩토리얼
F = [1 for i in range(4000001)]
for i in range(1, 4000001) : 
    F[i] = F[i-1] * i % 1000000007

# a^b%p
def power(a, b, p):
    if b == 0:
        return 1
    if b % 2 :
        return (power(a, b // 2, p) ** 2 * a) % p
    else:
        return (power(a, b // 2, p) ** 2) % p

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