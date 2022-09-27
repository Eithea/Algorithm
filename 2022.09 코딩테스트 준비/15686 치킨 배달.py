import sys
from itertools import combinations
input = sys.stdin.readline

city, house, chick = [], [], []
n, m = map(int, input().split())
for i in range(n) : 
    row = list(map(int, input().split()))
    for j in range(n) : 
        if row[j] == 1 : 
            house.append([i,j])
        elif row[j] == 2 : 
            chick.append([i,j])
    city.append(row)

lengths = []
for i, j in house : 
    leng = []
    for x, y in chick : 
        leng.append(abs(i-x) + abs(j-y))
    lengths.append(leng)

def calcLeng(pick) : 
    leng = 0
    for D in lengths : 
        d = sys.maxsize
        for i in pick : 
            d = min(d, D[i])
        leng += d
    return leng

combs = combinations([i for i in range(len(chick))], m)

minLeng = sys.maxsize
for pick in combs : 
    minLeng = min(minLeng, calcLeng(pick))
print(minLeng)