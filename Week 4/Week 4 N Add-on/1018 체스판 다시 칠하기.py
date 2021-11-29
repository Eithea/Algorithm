n, m = map(int, input().split())
T = []
for i in range(n) : 
    T.append(input())

mincount = 65
for x in range(n - 7) : 
    for y in range(m - 7) : 
        count = 0
        for i in range(8) : 
            for j in range(8) : 
                dir = (i + j) % 2
                if dir == 0 and T[x+i][y+j] == 'B' or dir == 1 and T[x+i][y+j] == 'W' : 
                    count = count + 1
        count = min(count, 64 - count)
        if count < mincount : 
            mincount = count
print(mincount)