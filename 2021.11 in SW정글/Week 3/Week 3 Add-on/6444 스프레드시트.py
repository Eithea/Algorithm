import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digit = list('0123456789')

dic = {}
for i in range(26) : 
    dic[alph[i]] = i + 1
for i in range(26) : 
    for j in range(26) : 
        dic[alph[i] + alph[j]] = (i + 1) * 26 + j + 1
for i in range(26) : 
    for j in range(26) : 
        for k in range(26) : 
            dic[alph[i] + alph[j] + alph[k]] = (i + 1) * 26 * 26 + (j + 1) * 26 + k + 1

def transRC(inp) : 
    if len(inp) > 2 and inp[2] not in digit : 
        col = dic[inp[:3]]
        row = int(inp[3:])
    elif inp[1] not in digit : 
        col = dic[inp[:2]]
        row = int(inp[2:])
    else : 
        col = dic[inp[0]]
        row = int(inp[1:])
    return [row, col]

def translation(inp) : 
    if inp[0] == '=' : 
        calbox = inp[1:].split('+')
        for i in range(len(calbox)) : 
            calbox[i] = transRC(calbox[i])
        return calbox
    else : 
        return int(inp)

testcase = int(input())
for t in range(testcase) : 
    Cn, Rn = map(int, input().split())
    T = [[None]]
    for i in range(Rn) : 
        T.append([None] + list(input().split()))

    def DFS(r, c) : 
        tr = translation(T[r][c])
        if type(tr) is int : 
            T[r][c] = tr
        else : 
            sum = 0
            for row, col in tr : 
                if type(T[row][col]) is not int : 
                    DFS(row, col)
                sum = sum + T[row][col]
            T[r][c] = sum

    for i in range(1, Rn + 1) : 
        for j in range(1, Cn + 1) : 
            if type(T[i][j]) is not int : 
                DFS(i, j)
    for i in range(1, Rn + 1) : 
        print(*T[i][1:])