n = int(input())
l = list(map(int, input().split()))
l.append(0)
l.append(0)
for i in range(n) : 
    l[n-i] = l[n-i-1]
l[0] = 0

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
