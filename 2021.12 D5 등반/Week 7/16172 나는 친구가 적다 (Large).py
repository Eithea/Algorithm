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

digit = [str(i) for i in range(10)]
def KMP(string, text) :
    lps = LPS(string)
    ans = []
    i, j = 0, 0
    while i < len(text) : 
        if text[i] in digit : 
            i = i + 1
        elif string[j] == text[i] :
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
string = input()
if KMP(string, text) : 
    print(1)
else : 
    print(0)