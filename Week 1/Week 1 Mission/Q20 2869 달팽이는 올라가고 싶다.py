import math
a, b, x = map(int, input().split())
print(math.ceil((x-a)/(a-b))+1)