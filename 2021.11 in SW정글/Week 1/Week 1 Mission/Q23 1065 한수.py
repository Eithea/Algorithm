testrange = int(input())
stack = 0
for k in range(1, testrange + 1):
    if k < 100 : 
        stack = stack + 1
    else : 
        n = [int(u) for u in str(k)]
        a = n[0] - n[1]
        check = 0
        for i in range(1, len(n) - 1):
            if n[i] - n[i+1] != a:
                check = 1
                break
        if check == 0 : 
            stack = stack + 1
print(stack)