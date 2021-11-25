testcase = int(input())
for i in range(testcase) : 
    OXlist = list(input())
    stack = 0
    score = 0
    for t in OXlist : 
        if t == 'O' : 
            stack = stack + 1
        else : 
            stack = 0           
        score = score + stack
    print(score)
