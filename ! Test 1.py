i = 50000
n = 20
while n > 0 : 
    print(i)
    i = i - (i&-i)
    n = n-1