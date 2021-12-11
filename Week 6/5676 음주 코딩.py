import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

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
    return a * b

def op(x) : 
    if x == 0 : 
        return 0
    if x > 0 :
        return 1
    else : 
        return -1

def makeTR(tree, list, i, start, end) : 
    if start == end : 
        x = list[start]
        tree[i] = op(x)
        return tree[i]
    center = (start + end) // 2
    a = makeTR(tree, list, 2*i, start, center)
    b = makeTR(tree, list, 2*i+1, center+1, end)
    tree[i] = SGoperator(a, b)
    return tree[i]

def SGsearchfunc(tree, i, start, end, left, right) : 
    if left > end or right < start : 
        return 1
    if left <= start and right >= end : 
        return tree[i]
    center = (start + end) // 2
    a = SGsearchfunc(tree, 2*i, start, center, left, right)
    b = SGsearchfunc(tree, 2*i+1, center+1, end, left, right)
    return SGoperator(a, b)

def SGupdate(tree, i, start, end, index, newdata) : 
    if index < start or index > end : 
        return
    if start == end : 
        tree[i] = newdata
        return
    center = (start + end) // 2
    SGupdate(tree, 2*i, start, center, index, newdata)
    SGupdate(tree, 2*i+1, center+1, end, index, newdata)
    tree[i] = tree[2*i] * tree[2*i+1]
    

while True :
    try :
        n, k = map(int, input().split())
        l = list(map(int, input().split()))
        T = SGTR(l)
        ans = ''
        for i in range(k) : 
            a, b, c = input().split()
            b = int(b)
            c = int(c)
            if a == 'C' : 
                l[b-1] = c
                SGupdate(T, 1, 0, n-1, b-1, op(c))
            elif a == 'P' : 
                x = SGsearchfunc(T, 1, 0, n-1, b-1, c-1)
                if x == 0 : 
                    ans = ans + '0'
                elif x > 0 : 
                    ans = ans + '+'
                else : 
                    ans = ans + '-'
        print(ans)
    except Exception :
        break