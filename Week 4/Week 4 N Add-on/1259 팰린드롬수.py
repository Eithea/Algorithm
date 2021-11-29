while True : 
    l = input()
    if l == '0' : 
        break
    p = 'yes'
    for i in range(len(l)//2 + 1) : 
        if l[i] != l[-1-i] : 
            p = 'no'
    print(p)