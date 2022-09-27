def sumDigit(n) : 
    ret = 0
    while n : 
        ret += n %10
        n = n //10
    return ret

n = 10000
l = [0 for i in range(n+100)]

for i in range(n) : 
    l[i+sumDigit(i)] = 1

for i in range(1, n+1) : 
    if not l[i] : 
        print(i)