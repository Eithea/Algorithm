import sys
input = sys.stdin.readline
n = int(input())

stack = []
count = 0
for i in range(n) : 
    x = int(input())
    same = 0
    if not stack : 
        stack.append([x, 1])
        continue
    while stack and stack[-1][0] < x : 
        count = count + stack.pop()[1]
    if stack and stack[-1][0] == x : 
        same = stack.pop()[1]
    count = count + same
    if stack : 
        count = count + 1 
    stack.append([x, same + 1])
print(count)