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
    return convex

t = int(input())
while t : 
    t = t - 1
    n = int(input())
    points = []
    for i in range((n-1)//5 + 1) : 
        points = points + list(map(int, input().split()))
    P = []
    for i in range(n):
        P.append([points[2*i], points[2*i+1]])

    P = sorted(P, key=lambda x:(x[1], -x[0]))
    ans = convex_hull(P)[1:]

    P.reverse()
    ans = convex_hull(P)[1:] + ans
    ans.reverse()
    print(len(ans))
    for i in range(len(ans)) : 
        print(*ans[i])