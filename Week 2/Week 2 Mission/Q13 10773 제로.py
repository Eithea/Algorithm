import sys  
input = sys.stdin.readline

stack = []
def stk(t) : 
    if t == 0 : 
        del stack[-1]
    else : 
        stack.append(t)

n = int(input())
for i in range(n) : 
    x = int(input())
    stk(x)
print(sum(stack))