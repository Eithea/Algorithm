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
l = list(input().split())
l = list(input().split())
string = ''
for s in l : 
    string = string + s

lps = LPS(string)
lens = len(string)
if lens % (lens - lps[-1]) : 
    sub = 1
else : 
    sub = lens // (lens - lps[-1])

from math import gcd
g = gcd(n, sub)
print(str(sub//g) + '/' + str(n//g))