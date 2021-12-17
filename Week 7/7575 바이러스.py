def LPS(string) :
    lps = [0 for i in range(len(string))]
    maxfix = 0
    i = 1
    while i < len(string) :
        if string[i] == string[maxfix] :
            maxfix = maxfix + 1
            lps[i] = maxfix
            i = i + 1
        elif maxfix != 0 :
            maxfix = lps[maxfix-1]
        else :
            lps[i] = 0
            i = i + 1
    return lps

def KMP(string, text) :
    lps = LPS(string)
    if len(string) > len(text) : 
        return False
    i, j = 0, 0
    while i < len(text) :
        if string[j] == text[i] :
            i = i + 1
            j = j + 1
        elif j != 0 :
            j = lps[j-1]
        else:
            i = i + 1
        if j == len(string) :
            return True
    return False

n, k = map(int, input().split())
len0 = int(input())
l0 = list(map(int, input().split()))
L = []
for i in range(n-1) : 
    leni = int(input())
    li = list(map(int, input().split()))
    L.append([leni, li])

for s in range(len0 - k + 1) : 
    subsR = l0[s:s+k]
    subs = subsR[:]
    subsR.reverse()
    i = 0
    while i < n - 1 : 
        TF = KMP(subs, L[i][1])
        if not TF : 
            TF = KMP(subsR, L[i][1])
        if not TF : 
            break
        i = i + 1
    if TF : 
        print('YES')
        exit(0)
    else :     
        continue
print('NO')