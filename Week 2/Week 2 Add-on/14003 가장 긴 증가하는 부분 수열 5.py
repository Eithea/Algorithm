from bisect import bisect_left

n = int(input())
l = list(map(int,input().split()))

order = [0 for i in range(n)]
order[0] = 1
table = [l[0]]
for i in range(1, n) : 
    if table[-1] < l[i] : 
        table.append(l[i])
        order[i] = len(table)
    else : 
        order[i] = bisect_left(table, l[i]) + 1
        table[order[i] - 1] = l[i]
m = max(order)
print(m)
lis = []
for i in range(n) : 
    if order[n-1-i] == m : 
        lis.append(l[n-1-i])
        m = m - 1
for i in range(len(lis)) : 
    print(lis[len(lis)-1-i], end = ' ')