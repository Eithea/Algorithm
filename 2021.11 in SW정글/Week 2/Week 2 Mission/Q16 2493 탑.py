n = int(input())
l = list(map(int, input().split()))

stack = [[0, l[0]]]
table = [0]
for i in range(1, n) : 
    h = l[i]
    while stack[-1][1] < h : 
        del stack[-1]
        if stack == [] : 
            table.append(0)
            break
    if stack != [] : 
        table.append(stack[-1][0] + 1)
    stack.append([i, h])
    
for i in range(len(table) - 1) : 
    print(table[i], end = ' ')
print(table[-1])