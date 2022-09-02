def BFS(E) : 
    que = [E]
    while que : 
        a, b = que[0][0], que[0][1]
        del que[0]
        for c in C : 
            if c[2] == 0 : 
                if abs(c[0] - a) + abs(c[1] - b) <= 1000 : 
                    c[2] = 1
                    que.append(c)

testcase = int(input())
for t in range(testcase) : 
    n = int(input())
    C = []
    H = list(map(int, input().split())) + [1]
    for i in range(n+1) : 
        C.append(list(map(int, input().split())) + [0])
    BFS(H)
    if C[n][2] == 1 : 
        print("happy")
    else : 
        print("sad")