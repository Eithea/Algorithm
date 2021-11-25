n = int(input())
for j in range(n) : 
    l = input()
    st = 0
    for i in range(len(l)) : 
        if l[i] == '(' :
            st = st + 1
        elif l[i] == ')' : 
            st = st - 1
            if st < 0 : 
                print('NO')
                break
    if st == 0 : 
        print('YES')
    elif st > 0 : 
        print('NO')