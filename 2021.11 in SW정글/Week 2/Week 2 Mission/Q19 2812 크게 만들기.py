import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = input()
stack = [int(l[0])]
count = 0
for i in range(1, n) : 
    while stack != [] and count < k : 
        if stack[-1] < int(l[i]) : 
            del stack[-1]
            count = count + 1
        else : 
            break
    stack.append(int(l[i]))
for i in range(n - k) : 
    print(stack[i], end = '')