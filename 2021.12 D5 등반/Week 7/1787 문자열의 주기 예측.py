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

n = int(input())
string = input()
lps = LPS(string)
DP = [0 for i in range(n)]
count = 0
for i in range(1, n) : 
    if lps[lps[i] - 1] > 0 : 
        DP[i] = DP[lps[i] - 1]
    else : 
        DP[i] = lps[i]
    if not DP[i] : 
        continue
    if DP[i] * 2 <= i + 1 : 
        count = count + i - DP[i] + 1
print(count)