n = int(input())
l = list(map(int, input().split()))
order = [0 for i in range(n)]
for after in range(n) : 
    for before in range(after) : 
        if l[after] > l[before] and order[after] < order[before] : 
            order[after] = order[before]
    order[after] = order[after] + 1

l.reverse()
RVorder = [0 for i in range(n)]
for after in range(n) : 
    for before in range(after) : 
        if l[after] > l[before] and RVorder[after] < RVorder[before] : 
            RVorder[after] = RVorder[before]
    RVorder[after] = RVorder[after] + 1

maxlen = 0
for i in range(n) : 
    maxlen = max(maxlen, order[i] + RVorder[-1-i] - 1)
print(maxlen)