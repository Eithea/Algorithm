n = int(input())
W=[]
for i in range(n) : 
    W.append(list(map(int, input().split())))
# n = 4
# W = [[0,10,15,20], [5,0,9,10], [6,13,0,12], [8,8,9,0]]

# j가 gone에 없고 W[gone[-1]][j]가 0이 아니라면
# gone에 넣고 togo에서 빼고 cost를 추가한 data 출력
def next(W, cost, gone, togo, j) : 
    t = togo[:]
    g = gone[:]
    if j in togo and W[gone[-1]][j] != 0 : 
        t.remove(j)
        g.append(j)
        c = cost + W[gone[-1]][j]
        return [c, g, t]
    else : 
        return ['trash']


datalist = [[], []]

# level 0에 스타팅포인트 [cost=0, gone=[i], togo=[i빼고나머지]] 입력
for i in range(n) : 
    datalist[0].append([0, [i], [i for i in range(n)]])
    datalist[0][i][2].remove(i)

# level x의 각 data에 대해, 도시 j로의 이동이 유효하면 level x+1에 data 추가
for x in range (0, n-1) : 
    for data in datalist[0] : 
        for j in data[2] : 
            newdata = next(W, data[0], data[1], data[2], j)
            if newdata != ['trash'] : 
                datalist[1].append(newdata)
    datalist[0] = datalist[1]
    datalist[1] = []

print(datalist)
#귀환
final = []
for data in datalist[0] : 
    final.append(next(W, data[0], data[1], [data[1][0]], data[1][0]))
    
# final의 data에서 min cost 출력

min = final[0][0]
for data in final : 
    if data[0] < min : 
        min = data[0]
print(min)