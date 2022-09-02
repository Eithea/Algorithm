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

l = input()
lps = LPS(l)
for i in range(1, len(l)+1) : 
    if i % (i-lps[i-1]) == 0 and i // (i-lps[i-1]) > 1 : 
        print(i, i // (i-lps[i-1]))