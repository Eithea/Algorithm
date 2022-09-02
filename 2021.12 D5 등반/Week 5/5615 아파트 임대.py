def MRprimetest(n) : 
    if n == 2 or n == 3 : 
        return True
    if n < 2 or n % 2 == 0 : 
        return False

    if n < 1373653 : 
        alist = [2, 3]
    elif n < 9080191 : 
        alist = [31, 73]
    elif n < 4759123141 : 
        alist = [2, 7, 61]
    elif n < 2152302898747 : 
        alist = [2, 3, 5, 7, 11]
    elif n < 3474749660383 : 
        alist = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321 : 
        alist = [2, 3, 5, 7, 11, 13, 17]
    else : 
        return None
    
    d = n - 1
    s = 0
    while d % 2 == 0 : 
        d = d // 2
        s = s + 1
    for a in alist : 
        x = pow(a, d, n)
        if x == 1 : 
            continue
        stest = False
        for i in range(s) : 
            if x == n - 1 : 
                stest = True
                break
            x = pow(x, 2, n)
        if not stest : 
            return False
    return True

import sys
input = sys.stdin.readline

n = int(input())
count = 0
for i in range(n) : 
    s = int(input())
    if MRprimetest(2*s + 1) : 
        count = count + 1
print(count)