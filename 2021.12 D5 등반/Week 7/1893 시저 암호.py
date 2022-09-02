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
            if not ans : 
                ans.append(i - j)
            else : 
                return []
            j = lps[j-1]
    return ans


def shift(code, x) : 
    return [(code[i]+x) % len(order) for i in range(len(code))]

testcase = int(input())
for t in range(testcase) : 
    order = input()
    string = input()
    text = input()
    V = {}
    for i in range(len(order)) : 
        V[order[i]] = i
    stringcode = [V[string[i]] for i in range(len(string))]
    textcode = [V[text[i]] for i in range(len(text))]
    shifts = []
    for i in range(len(order)) : 
        code = shift(stringcode, i)
        ans = KMP(code, textcode)
        if ans : 
            shifts.append(i)
    if not shifts : 
        print('no solution')
    elif len(shifts) == 1 : 
        print('unique:', *shifts)
    else : 
        print('ambiguous:', *shifts)