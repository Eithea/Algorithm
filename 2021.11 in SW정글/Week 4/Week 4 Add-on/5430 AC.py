from collections import deque
testcase = int(input())
for t in range(testcase) : 
    try : 
        F = input()
        n = int(input())
        l = input().split(',')
        l[0] = l[0][1:]
        l[-1] = l[-1][:-1]
        if l ==[''] : 
            l = []
        que = deque(l)
        dir = 1
        for i in range(len(F)) : 
            if F[i] == 'R' : 
                dir = -dir
            elif F[i] == 'D' : 
                if dir > 0 : 
                    que.popleft()
                else : 
                    que.pop()
                
        print('[', end = '')
        if len(que) != 0 : 
            if dir > 0 : 
                for i in range(len(que) - 1) : 
                    print(que[i], end = ',')
                print(que[-1], end = '')
            else : 
                for i in range(len(que) - 1) : 
                    print(que[-1-i], end = ',')
                print(que[0], end = '')
        print(']')
    except : 
        print('error')