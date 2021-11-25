import sys  
input = sys.stdin.readline

n = int(input())
l = [0 for i in range(n+1)]
l[0] = 0
stack = [[0, 0]]
for i in range(1, n+1) : 
    h = int(input())
    if h >= l[i-1] : 
        while len(stack) > 0 and stack[-1][1] <= h : 
            del stack[-1]
        stack.append([i, h])
    else : 
        stack.append([i, h])
print(len(stack))