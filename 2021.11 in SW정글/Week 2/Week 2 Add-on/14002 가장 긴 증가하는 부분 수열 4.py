n = int(input())
l = list(map(int, input().split()))
order = [0 for i in range(n)]
for after in range(n) : 
    for before in range(after) : 
        if l[after] > l[before] and order[after] < order[before] : 
            order[after] = order[before]
    order[after] = order[after] + 1
m = max(order)
print(m)
lis = []
for i in range(n) : 
    if order[n-1-i] == m : 
        lis.append(l[n-1-i])
        m = m - 1
for i in range(len(lis)) : 
    print(lis[len(lis)-1-i], end = ' ')
