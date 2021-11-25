import sys
input = sys.stdin.readline

Vn, En = map(int, input().split())
V = {}
E = []
for i in range(1, Vn + 1) : 
    V[i] = i
for i in range(En) : 
    E.append(list(map(int, input().split())))
E.sort(key = lambda x : x[2])

def endof(x) : 
    if V[x] == x : 
        return x
    return endof(V[x])

def check(a, b) : 
    if endof(a) == endof(b) : 
        return True
    return False

def connect(a, b) : 
    if endof(a) < endof(b) : 
        V[endof(a)] = endof(b)
    else : 
        V[endof(b)] = endof(a)

cost = 0
for v1, v2, c in E : 
    if not check(v1, v2) : 
        connect(v1, v2)
        cost = cost + c
print(cost)