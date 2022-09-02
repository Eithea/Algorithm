import sys  
input = sys.stdin.readline
l = []
n = int(input())
for i in range(n) : 
    l.append(list(map(int, input().split())))
l.sort()

def length(p, q) : 
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def DAC(start, end) : 
    if end == start + 1 : 
        return length(l[start], l[end])
    center = (start + end) // 2
    minl = min(DAC(start, center), DAC(center, end))
    
    rng = []
    for i in range(start, end + 1) : 
        if (l[center][0] - l[i][0]) ** 2 < minl : 
            rng.append(l[i])
    rng.sort(key = lambda x : x[1])

    for i in range(len(rng)) : 
        for j in range(i + 1, len(rng)) : 
            if (rng[i][1] - rng[j][1]) ** 2 < minl : 
                minl = min(minl, length(rng[i], rng[j]))
            else : 
                break
    return minl

print(DAC(0, n-1))