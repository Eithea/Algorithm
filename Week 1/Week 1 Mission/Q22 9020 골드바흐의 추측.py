def prime(n) : 
    if n < 2 : 
        return False
    for j in range(2, n//2+1) : 
        if n%j == 0 : 
            return False
    return True

primelist = []
for i in range(10000) : 
    if prime(i) : 
        primelist.append(i)
        
testcase = int(input())
for j in range(testcase) : 
    n = int(input())
    for i in range(n//2+1) : 
        a = n//2 - i
        b = n//2 + i
        if a in primelist and b in primelist :
            print(a, b, sep = ' ')
            break