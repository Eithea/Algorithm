import sys
input = sys.stdin.readline
from collections import deque

def D(x) : 
    y = (2 * x) % 10000
    return y
def S(x) : 
    y = (x - 1) % 10000
    return y
def L(x) : 
    y = (x % 1000) * 10 + x // 1000
    return y
def R(x) : 
    y = (x % 10) * 1000 + x // 10
    return y
def f(x) : 
    return [D(x), S(x), L(x), R(x)]
trs = ['D', 'S', 'L', 'R']
testcase = int(input())
for t in range(testcase) : 
    start, end = map(int, input().split())
    gone = [False for i in range(10000)]
    ans = []
    que = deque()
    que.append([start, []])
    gone[start] = True
    while que : 
        x, c = que.popleft()
        if x == end : 
            ans = c
            break
        ff = f(x)
        for i in range(4) : 
            y = ff[i]
            if not gone[y] : 
                gone[y] = True
                que.append([y, c + [i]])
    for i in range(len(ans)) : 
        print(trs[ans[i]], end = '')
    print()