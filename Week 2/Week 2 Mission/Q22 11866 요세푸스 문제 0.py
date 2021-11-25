n, k = map(int, input().split())
print('<', end = '')
que = [x+1 for x in range(n)]
point = 0
count = 0
stack = 0
while stack < n : 
    count = count + 1
    if count == k : 
        print(que[point], end = '')
        count = 0
        stack = stack + 1
        if stack != n : 
            print(', ', end = '')
    else : 
        que.append(que[point])
    point = point + 1
print('>')