import sys
input = sys.stdin.readline

n = int(input())
l = []
for i in range(n) : 
    l.append(list(map(int, input().split())))
l.sort(key = lambda x : x[0])
l.sort(key = lambda x : x[1])
now = 0
count = 0
for start, end in l : 
    if start >= now : 
        count = count + 1
        now = end
print(count)