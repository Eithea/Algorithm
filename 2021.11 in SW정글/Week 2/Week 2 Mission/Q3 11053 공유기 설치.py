import sys
input = sys.stdin.readline

n, c = map(int, input().split())
l = []
for i in range(n) : 
    l.append(int(input()))
l.sort()

def Bsearch(list) : 
    drangel = 1
    dranger = list[-1] - list[0]
    while drangel <= dranger : 
        d = (drangel + dranger) // 2
        now = list[0]
        count = 1
        for i in range(1, n) : 
            if list[i] - now >= d : 
                now = list[i]
                count = count + 1
        if count >= c : 
            maxd = d
            drangel = d + 1
        else : 
            dranger = d - 1
    return maxd

print(Bsearch(l))