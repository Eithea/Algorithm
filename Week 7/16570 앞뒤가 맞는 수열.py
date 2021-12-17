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
l = list(map(int, input().split()))
l.reverse()
lps = LPS(l)

k = lps[-1]
count = 0
if k : 
    count = 1
for i in range(n-1) : 
    if lps[i] > k : 
        k = lps[i]
        count = 1
    elif lps[i] == k > 0 : 
        count = count + 1
if k : 
    print(k, count)
else : 
    print(-1)