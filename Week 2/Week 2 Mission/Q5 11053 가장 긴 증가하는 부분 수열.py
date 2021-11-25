n = int(input())
l = list(map(int, input().split()))
order = [0 for i in range(n)]
for after in range(n) : 
    for before in range(after) : 
        if l[after] > l[before] and order[after] < order[before] : 
            order[after] = order[before]
    order[after] = order[after] + 1
print(max(order))