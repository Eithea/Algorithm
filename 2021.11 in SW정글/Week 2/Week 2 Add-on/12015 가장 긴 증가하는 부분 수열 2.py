from bisect import bisect_left
n = int(input())
l = list(map(int, input().split()))

table = [l[0]]
for i in range(1, n):
    if l[i] > table[-1]:
        table.append(l[i])
    else:
        table[bisect_left(table, l[i])] = l[i]
print(len(table))