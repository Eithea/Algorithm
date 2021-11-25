table = []
for i in range(1, 10) :
    for j in range(1, 10) : 
        for k in range(1, 10) :  
            if i != j and j != k and k != i : 
                table.append([i, j, k])
def sb(q, t) : 
    s = 0
    b = 0
    for i in range(3) : 
        if t[i] == q[i] : 
            s = s + 1
    for w in q : 
        if w in t : 
            b = b + 1
    b = b - s
    return [s, b]

n = int(input())
for i in range(n) : 
    h = list(input().split())
    Q = [int(h[0][0]), int(h[0][1]), int(h[0][2])]
    HIT = [int(h[1]), int(h[2])]
    for i in range(len(table)) : 
        if sb(Q, table[i]) != HIT : 
            table[i] = 0
    while 0 in table : 
        table.remove(0)
print(len(table))