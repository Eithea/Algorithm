testcase = int(input())
l = []
for i in range(testcase) : 
    l.append(int(input()))
n= len(l)
for i in range(n-1) : 
    for j in range(n-1, i, -1) : 
        if l[j-1] > l[j] : 
            l[j-1], l[j] = l[j], l[j-1]
for i in range(n) : 
    print(l[i])