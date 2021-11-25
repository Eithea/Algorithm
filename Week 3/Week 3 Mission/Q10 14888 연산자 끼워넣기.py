n = int(input())

a = list(map(int, input().split()))
C = list(map(int, input().split()))

minv = 1000000000
maxv = -minv

def DFS(value, i, op, left1, left2, left3, left4) : 
    if op == 1 : 
        value = value + a[i]
    elif op == 2 : 
        value = value - a[i]
    elif op == 3 : 
        value = value * a[i]
    else : 
        value = int(value / a[i])
    if i == n - 1 : 
        global maxv, minv
        maxv = max(maxv, value)
        minv = min(minv, value)
    else : 
        if left1 > 0 : 
            DFS(value, i + 1, 1, left1 - 1, left2, left3, left4)
        if left2 > 0 : 
            DFS(value, i + 1, 2, left1, left2 - 1, left3, left4)
        if left3 > 0 : 
            DFS(value, i + 1, 3, left1, left2, left3 - 1, left4)
        if left4 > 0 : 
            DFS(value, i + 1, 4, left1, left2, left3, left4 - 1)

for i in range(4) : 
    if C[i] != 0 : 
        C[i] = C[i] - 1
        DFS(a[0], 1, i + 1, C[0], C[1], C[2], C[3])
        C[i] = C[i] + 1
print(maxv)
print(minv)