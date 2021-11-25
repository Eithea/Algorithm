import sys  
input = sys.stdin.readline

stack = []
def stk(inp) : 
    if inp[0] == 'push' : 
        stack.append(int(inp[1]))
    elif inp[0] == 'pop' : 
        if stack == [] : 
            print(-1)
        else : 
            print(stack[-1])
            del stack[-1]
    elif inp[0] == 'size' : 
        print(len(stack))
    elif inp[0] == 'empty' : 
        if stack == [] : 
            print(1)
        else : 
            print(0)
    elif inp[0] == 'top' : 
        if stack == [] : 
            print(-1)
        else : 
            print(stack[-1])

    
n = int(input())
for i in range(n) : 
    x = list(input().split())
    stk(x)