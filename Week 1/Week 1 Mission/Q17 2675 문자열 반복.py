testcase = int(input())
for i in range(testcase) : 
    txt = ''
    a, b =input().split()
    n = int(a)
    t = list(b)
    for i in t : 
        txt = txt + i*n
    print(txt)