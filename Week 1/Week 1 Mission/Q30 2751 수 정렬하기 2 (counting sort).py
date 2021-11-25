import sys
input = sys.stdin.readline
testsize = int(input())
testrange = 2000000
frequency = [0 for i in range(testrange+1)]

for i in range(testsize) : 
    n = int(input())
    frequency[n + 1000000] = frequency[n+1000000] + 1


for i in range(len(frequency)) : 
    for j in range(frequency[i]) : 
        print(i - 1000000)