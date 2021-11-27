import sys
input = sys.stdin.readline

n, k = map(int, input().split())
C = []
for i in range(n) : 
    C.append(list(map(int, input().split())))

f = [0 for i in range(k + 1)]
t = False
for w, v in C:
    for j in range(1, k + 1):
        if t : 
            j = k-j+1
        if j < w:
            f[j] = f[j - 1]
        else:
            f[j] = max(f[j], f[j - w] + v)
    t = True
print(f[-1])