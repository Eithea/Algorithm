l9=[[0 for i in range(10)] for i in range(10)]
for i in range(1, 10) : 
    for j in range(1, 10) : 
        l9[i][0] = i * (10 ** (i - 1)) - (10 ** i) // 9
        l9[i][j] = i * 10 ** (i - 1)

num = input()
count = [0 for i in range(10)]
for i in range(len(num) - 1) : 
    count[int(num[i])] = count[int(num[i])] + int(num[i+1:]) + 1
n = int(num)
for i in range(int(num[-1]) + 1) : 
    count[i] = count[i] + 1
order = 1
while order < len(num) : 
    digit = int(num[-order-1])
    for i in range(digit) : 
        count[i] = count[i] + 10 ** order
    for i in range(10) : 
        count[i] = count[i] + int(digit) * order * 10 ** (order - 1)
    order = order + 1
count[0] = count[0] - 10 ** order // 9
print(*count)