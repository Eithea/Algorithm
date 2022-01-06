def mult(A, B) : 
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n) : 
        for j in range(n) : 
            sum = 0
            for x in range(n) : 
                sum = sum + A[i][x] * B[x][j]
            C[i][j] = sum % 1000
    return C

n = 2
A = [[6, -4], [1, 0]]
I = [[0 for i in range(n)] for j in range(n)]
for i in range(n) : 
    I[i][i] = 1

powerlist = [0 for i in range(33)]
powerlist[0] = A
for i in range(1, 33) : 
    powerlist[i] = mult(powerlist[i-1], powerlist[i-1])


testcase = int(input())
for t in range(testcase) : 
    b = int(input())
    b = b - 2
    ans = [[] for i in range(n)]
    bilist = [0 for i in range(33)]
    for i in range(32, -1, -1) : 
        bilist[i] = b // pow(2, i)
        b = b - bilist[i] * pow(2, i)
    if bilist[0] == 1 : 
        for i in range(n) : 
            ans[i] = powerlist[0][i][:]
    else : 
        for i in range(n) : 
            ans[i] = I[i][:]
    for i in range(1, 33) : 
        if bilist[i] == 1 : 
            ans = mult(ans, powerlist[i])
    x = (ans[0][0] * 28 + ans[0][1] * 6 - 1) %1000
    if x > 99 : 
        print('Case #', t+1, ': ', x, sep = '')
    elif x > 9 : 
        print('Case #', t+1, ': ', 0, x, sep = '')
    else : 
        print('Case #', t+1, ': ', 0, 0, x, sep = '')
