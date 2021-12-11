# graph dict
Vn, En = map(int, input().split())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v2].append(v1)

# topological sorting
parent = [0 for i in range(Vn + 1)]
parent[v1] = parent[v1] + 1
child = [0 for i in range(Vn + 1)]
child[v2] = child[v2] + 1


# segment tree
def SGTR(list) : 
    n = len(list)
    size = 1
    while size < n : 
        size = size * 2
    size = size * 2
    segTR = [0 for i in range(size)]
    makeTR(segTR, list, 1, 0, n-1)
    return segTR

def SGoperator(a, b) : 
    return a + b

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        tree[i] = list[start]
        return tree[i]
    center = (start + end) // 2
    a = makeTR(tree, list, 2*i, start, center)
    b = makeTR(tree, list, 2*i+1, center+1, end)
    tree[i] = SGoperator(a, b)
    return tree[i]

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 0
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    a = SGsearchfunc(tree, 2*i, start, center, left, right)
    b = SGsearchfunc(tree, 2*i+1, center+1, end, left, right)
    return SGoperator(a, b)

def SGupdate(tree, i, start, end, index, delta) : 
    if index < start or index > end : 
        return
    if start == end : 
        tree[i] = delta
        return
    center = (start + end) // 2
    SGupdate(tree, 2*i, start, center, index, delta)
    SGupdate(tree, 2*i+1, center+1, end, index, delta)
    tree[i] = SGoperator(tree[2*i], tree[2*i+1])