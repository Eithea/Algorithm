import sys
input = sys.stdin.readline
testsize = int(input())
testrange = 10000
frequency = [0 for i in range(testrange+1)]

for i in range(testsize) : 
    n = int(input())
    frequency[n] = frequency[n] + 1


for i in range(len(frequency)) : 
    for j in range(frequency[i]) : 
        print(i)