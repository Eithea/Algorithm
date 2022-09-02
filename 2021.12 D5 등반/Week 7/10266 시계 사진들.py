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

n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.sort()
l2.sort()
rng = 360000
gap1 = [(l1[i] - l1[i-1]) %rng for i in range(n)]
gap2 = [(l2[i] - l2[i-1]) %rng for i in range(n)]
gap2 = gap2 * 2

if KMP(gap1, gap2) : 
    print('possible')
else : 
    print('impossible')