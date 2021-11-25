a = int(input())
b = int(input())
c = int(input())

n = [0,0,0,0,0,0,0,0,0,0]

number = list(str(a*b*c))
for i in number : 
    n[int(i)] = n[int(i)] + 1
for i in range(10) : 
    print(n[i])