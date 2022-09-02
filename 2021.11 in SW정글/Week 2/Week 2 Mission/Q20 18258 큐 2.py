import sys  
input = sys.stdin.readline

que = []
point = 0
def stk(inp) : 
    global point
    if inp[0] == 'push' : 
        que.append(int(inp[1]))
    elif inp[0] == 'pop' : 
        if len(que) == point : 
            print(-1)
        else : 
            print(que[point])
            point = point + 1
    elif inp[0] == 'size' : 
        print(len(que) - point)
    elif inp[0] == 'empty' : 
        if len(que) == point : 
            print(1)
        else : 
            print(0)
    elif inp[0] == 'front' : 
        if len(que) == point : 
            print(-1)
        else : 
            print(que[point])
    elif inp[0] == 'back' : 
        if len(que) == point : 
            print(-1)
        else : 
            print(que[-1])

n = int(input())
for i in range(n) : 
    x = list(input().split())
    stk(x)