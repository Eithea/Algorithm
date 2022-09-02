n = int(input())
l = []
for i in range(n) : 
    l.append(list(map(int, input().split())))
l.sort()
order = [0 for i in range(n)]
for after in range(n) : 
    for before in range(after) : 
        if l[after][0] > l[before][0] and l[after][1] > l[before][1] and order[after] < order[before] : 
            order[after] = order[before]
    order[after] = order[after] + 1
m = max(order)
print(n-m)
