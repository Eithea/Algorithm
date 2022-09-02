import sys  
input = sys.stdin.readline
n = int(input())
l = [0]
for i in range(n) : 
    l.append(int(input()))
l.append(0)

stack = [[0, 0]]
maxarea = 0
for i in range(1, n+2) : 
    h = l[i]
    while stack[-1][1] > h : 
        sh = stack[-1][1]
        del stack[-1]
        while stack[-1][1] == sh : 
            del stack[-1]
        area = (i - stack[-1][0] - 1) * sh
        maxarea = max(maxarea, area)
    stack.append([i, h])
print(maxarea)