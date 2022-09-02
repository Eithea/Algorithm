a, b, c = map(int, input().split())
powerlist = [0 for i in range(31)]
powerlist[0] = a % c
for i in range(1, 31) : 
    powerlist[i] = pow(powerlist[i-1], 2) % c


bilist = [0 for i in range(31)]
for i in range(30, -1, -1) : 
    bilist[i] = b // pow(2, i)
    b = b - bilist[i] * pow(2, i)

remain = 1
for i in range(31) : 
    if bilist[i] == 1 : 
        remain = (remain * powerlist[i]) % c 
print(remain)
