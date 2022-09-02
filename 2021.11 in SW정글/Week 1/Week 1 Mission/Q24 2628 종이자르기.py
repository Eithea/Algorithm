w, h = map(int, input().split())
x = []
y = []
cut = int(input())
for i in range(cut) : 
    direction, cutpoint = map(int, input().split())
    if direction == 0 : 
        y.append(cutpoint)
    elif direction == 1 : 
        x.append(cutpoint)
y.append(0)
y.append(h)
x.append(0)
x.append(w)
y = sorted(y)
x = sorted(x)
a = []
b = []
for i in range(len(x) - 1) : 
    a.append(x[i+1] - x[i])
for i in range(len(y) - 1) : 
    b.append(y[i+1] - y[i])

print(max(a) * max(b))