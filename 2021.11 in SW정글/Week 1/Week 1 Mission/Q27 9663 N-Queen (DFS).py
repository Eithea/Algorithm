n = int(input())
stack = 0
Qlist = []

def Qcheck(Qlist, Q) : 
    for i in range(len(Qlist)) : 
        if Q == Qlist[i] or abs(len(Qlist) - i) == abs(Q - Qlist[i]) : 
            return False
    return True
def DFS(Qlist, Q) : 
    global stack
    if len(Qlist) == n - 1 : 
        if Qcheck(Qlist, Q) : 
            stack = stack + 1
    if Qcheck(Qlist, Q) : 
        for i in range(n) : 
            DFS(Qlist + [Q], i)

if n < 12 : 
    for i in range(n) : 
        DFS([], i)
elif n >= 12 and n%2 == 0 : 
    for i in range(n//2) : 
        DFS([], i)
    stack = stack * 2
else : 
    for i in range(n//2) : 
        DFS([], i)
    stack = stack * 2
    DFS([], n//2)

print(stack)