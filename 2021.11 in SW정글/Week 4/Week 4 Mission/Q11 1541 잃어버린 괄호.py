l = input()
i = 0
sum = 0
sign = 1
while i < len(l) : 
    n = ''
    while i < len(l) and l[i] != '+' and l[i] != '-' : 
        n = n + l[i]
        i = i + 1
    num = int(n)
    if i < len(l) and l[i] == '+' : 
        sum = sum + num * sign
        i = i + 1
    if i < len(l) and l[i] == '-' : 
        sum = sum + num * sign
        sign = -1
        i = i + 1
print(sum + num * sign)
