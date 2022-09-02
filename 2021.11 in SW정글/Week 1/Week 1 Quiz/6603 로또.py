l = ''
while l != [0] : 
    l = list(map(int, input().split()))
    S = l[1:]
    sol = []
    def DFS(picked, newpick) : 
        if len(picked) == 5 : 
            sol.append(picked + [newpick])
        for i in S : 
            if i > newpick :
                DFS(picked + [newpick], i)
    for x in S : 
        DFS([], x)
    for i in range(len(sol)) : 
        for j in range(len(sol[i]) - 1) : 
            print(sol[i][j], end = ' ')
        print(sol[i][-1])
    print()