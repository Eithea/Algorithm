import sys
input = sys.stdin.readline

n = int(input())
V = []
for i in range(n) : 
    V.append(list(map(int, input().split())))

V.append(V[0])
sum = 0
for i in range(n) : 
    x1, y1 = V[i]
    x2, y2 = V[i+1]
    S = (x1 * y2 - x2 * y1) / 2
    sum = sum + S
print(abs(sum))