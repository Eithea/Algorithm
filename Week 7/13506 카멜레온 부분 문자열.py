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
    ans = []
    if len(string) > len(text) : 
        return ans
    lps = LPS(string)
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
            ans.append(i - j)
            j = lps[j-1]
    return ans
    
text = input()
fix = text[:]
lpsf = LPS(fix)
while lpsf[-1] : 
    fix = fix[:lpsf[-1]]
    lpsf = LPS(fix)
    ans = KMP(fix, text)
    if len(ans) < 3 : 
        continue
    elif ans[0] == 0 and ans[-1] == len(text) - len(fix) : 
        print(fix)
        exit(0)
print(-1)