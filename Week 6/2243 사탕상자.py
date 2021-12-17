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

rng = 1000001
T = [0 for i in range(4*rng)]
testcase = int(input())
for t in range(testcase) : 
    l = list(map(int, input().split()))
    if l[0] == 1 : 
        order = l[1]
        data = SGsearchfunc(T, order, 1, 0, rng-1)
        print(data)
        SGupdate(T, data, -1, 1, 0, rng-1)

    elif l[0] == 2 : 
        data = l[1]
        delta = l[2]
        SGupdate(T, data, delta, 1, 0, rng-1)
