import sys  
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
L.sort()
al = 0
ar = n- 1 
amin = abs(L[al] + L[ar])
def Bsearch(l, pl, pr) :
    global amin, al, ar
    if pl >= pr : 
        return [amin, al, ar]
    sum = l[pl] + l[pr]
    if abs(sum) < amin : 
        amin = abs(sum)
        al = pl
        ar = pr
    if sum == 0 : 
        return [amin, al, ar]
    if sum > 0 : 
        return Bsearch(l, pl, pr - 1)
    else : 
        return Bsearch(l, pl + 1, pr)
ans = Bsearch(L, al, ar)
print(L[ans[1]], L[ans[2]])