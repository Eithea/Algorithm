import sys
input = sys.stdin.readline

n, k = map(int, input().split())
plug = list(map(int, input().split()))

cons = [0 for i in range(n)]
count = 0
for now in range(k) : 
    TF = False
    for i in range(n) : 
        if cons[i] == 0 or cons[i] == plug[now] : 
            cons[i] = plug[now]
            TF = True
            break
    if TF : 
        continue
    count = count + 1
    lastidx = 0
    for i in range(n) : 
        try : 
            if lastidx < plug[now:].index(cons[i]) : 
                lastidx = plug[now:].index(cons[i])
                last = i
        except : 
            cons[i] = plug[now]
            TF = True
            break
    if TF : 
        continue
    cons[last] = plug[now]
print(count)