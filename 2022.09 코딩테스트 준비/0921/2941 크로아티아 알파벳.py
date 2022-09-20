x = input().rstrip()
ans = len(x)

for i in range(1, len(x)) : 
    if x[i] == '=' : 
        if x[i-1] == 'c' or x[i-1] == 's' : 
            ans -= 1
        if x[i-1] == 'z' : 
            ans -= 1
            if i > 1 and x[i-2] == 'd' : 
                ans -= 1
    elif x[i] == '-' : 
        if x[i-1] == 'c' or x[i-1] == 'd' : 
            ans -= 1
    elif x[i] == 'j' : 
        if x[i-1] == 'l' or x[i-1] == 'n' : 
            ans -= 1
print(ans)