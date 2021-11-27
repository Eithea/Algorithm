n = int(input())
list = [0, 1, 0]
for i in range(n) : 
    list[2] = (list[0] + list[1]) % 15746
    list[0], list[1] = list[1], list[2]
print(list[min(n, 2)])