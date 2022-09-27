n = int(input())
l = []
for i in range(n) : 
    l.append(list(map(int, input().split())))

for i in range(n) : 
    rank = 1
    for j in range(n) : 
        if l[i][0] < l[j][0] and l[i][1] < l[j][1] : 
            rank += 1
    print(rank, end = " ")