import sys
input = sys.stdin.readline

R = 4000
n = int(input())
l = []
s = 0
m, M = R+1, -R-1
dist = [0 for i in range(2*R +1)]
for i in range(n) : 
    x = int(input())
    l.append(x)
    dist[x+R] += 1
    s += x
    M = max(M, x)
    m = min(m, x)

def avrg(s) : 
    r = s %n
    if 2*r < n : 
        return s //n
    else : 
        return s //n +1

def cent(dist) : 
    x = -1
    for i in range(len(dist)) : 
        x += dist[i]
        if x >= n //2 : 
            return i-R

def most(dist) : 
    mx = max(dist)
    idx, flag = 0, 0
    for i in range(len(dist)) : 
        if dist[i] == mx : 
            idx = i
            if flag :
                break
            flag = 1
    return idx-R

print(avrg(s))
print(cent(dist))
print(most(dist))
print(M-m)