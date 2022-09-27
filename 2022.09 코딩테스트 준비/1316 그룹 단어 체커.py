def check(x) : 
    l = [0 for i in range(123)]
    l[ord(x[0])] = 1
    for i in range(1, len(x)) : 
        if x[i] == x[i-1] : 
            continue        
        if l[ord(x[i])] : 
            return 0
        l[ord(x[i])] = 1
    return 1

n = int(input())
ans = 0
for i in range(n) : 
    ans += check(input().rstrip())
print(ans)
