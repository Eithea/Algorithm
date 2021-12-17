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
        if string[j] == text[i] or text[i] == '?' :
            i = i + 1
            j = j + 1
        elif j != 0 : 
            i = i - j + 1
            j = 0
        else:
            i = i + 1
        if j == len(string) :
            ans.append(i - j)
            j = lps[j-1]
    return ans

text = input()
string = input()
print(len(KMP(string,text)))