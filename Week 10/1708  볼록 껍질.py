import sys
input = sys.stdin.readline

def vector(v1, v2):
    return [v2[0] - v1[0], v2[1] - v1[1]]
 
def ccw(v1, v2, v3):
    v, u = vector(v1, v2), vector(v2, v3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False
     
def convex_hull(P):
    convex = []
    for v3 in P:
        while len(convex) >= 2:
            v1, v2 = convex[-2], convex[-1]
            if ccw(v1, v2, v3):
                break
            convex.pop()
        convex.append(v3)    
    return len(convex)
 
n = int(input())

P = []
for i in range(n):
    P.append(list(map(int, input().split())))

P = sorted(P, key=lambda x:(x[0], x[1]))
count = -2
count = count + convex_hull(P)

P.reverse()
count = count + convex_hull(P)
print(count)