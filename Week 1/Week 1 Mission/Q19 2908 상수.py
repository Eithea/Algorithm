a, b = input().split()
x = list(a)
y = list(b)
for i in range(len(x)) : 
    x[i] = a[len(x)-i-1]
for i in range(len(y)) : 
    y[i] = b[len(y)-i-1]

c = int(''.join(x))
d = int(''.join(y))

if c>d : 
    print(c)
else : 
    print(d)