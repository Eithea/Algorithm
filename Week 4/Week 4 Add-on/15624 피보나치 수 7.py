n = int(input())
bilist = []
while n != 0 : 
    bilist.append(n%2)
    n = n//2

def mult(A, B) : 
    C = [[0 for i in range(2)] for j in range(2)]
    for i in range(2) : 
        for j in range(2) : 
            sum = 0
            for x in range(2) : 
                sum = sum + A[i][x] * B[x][j]
            C[i][j] = sum % 1000000007
    return C
X = [[1, 1], [1, 0]]
powerlist = []
for i in range(len(bilist)) : 
    powerlist.append(X)
    X = mult(X, X)
Xn = [[1,0],[0,1]]
for i in range(len(bilist)) : 
    if bilist[i] == 1 : 
        Xn = mult(Xn, powerlist[i])
print(Xn[0][1])