import sys
input = sys.stdin.readline

def SGoperator(a, b) : 
    return a + b

def SGsearchfunc(tree, order, node, start, end) : 
    if start == end : 
        return start
    center = (start + end) // 2
    if order <= tree[2*node] : 
        return SGsearchfunc(tree, order, 2*node, start, center)
    else : 
        return SGsearchfunc(tree, order - tree[2*node], 2*node+1, center+1, end)

def SGupdate(tree, data, delta, node, start, end) : 
    if data < start or data > end : 
        return
    if start == end : 
        tree[node] = tree[node] + delta
        return
    center = (start + end) // 2
    SGupdate(tree, data, delta, 2*node, start, center)
    SGupdate(tree, data, delta, 2*node+1, center+1, end)
    tree[node] = SGoperator(tree[2*node], tree[2*node+1])

n, k = map(int, input().split())
l = []
rng = 65536
T = [0 for i in range(4*rng)]
for i in range(n) : 
    l.append(int(input()))

for i in range(k) : 
    data = l[i]
    SGupdate(T, data, 1, 1, 0, rng-1)
count = 0
order = (k + 1) // 2
for i in range(k, n) : 
    datain = l[i]
    dataout = l[i - k]
    count = count + SGsearchfunc(T, order, 1, 0, rng-1)
    SGupdate(T, datain, 1, 1, 0, rng-1)
    SGupdate(T, dataout, -1, 1, 0, rng-1)
count = count + SGsearchfunc(T, order, 1, 0, rng-1)
print(count)