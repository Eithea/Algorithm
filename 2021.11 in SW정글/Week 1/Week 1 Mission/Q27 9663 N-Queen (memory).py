def Qlist_levelUP(Qlist_level_n, Q) : 
    check = 1
    Qlist = Qlist_level_n[:]
    if Q in Qlist : 
        check = 0
    for i in range(len(Qlist)) : 
        if abs(len(Qlist) - i) == abs(Q - Qlist[i]) : 
            check = 0
    if check == 1 : 
        Qlist.append(Q)
        return Qlist
    else : 
        return [0]
# level n의 Qlist에서 다음 n+1번째 퀸을 Q값에 뒀을때
# 유효하면 level n+1의 Qlist를 출력, 무효하면 [0] 출력


n = int(input())
answerlist = [[] for i in range(n)]

# level 1의 answerlist 생성
for i in range(n) : 
    answerlist[0].append([i])


# level x의 answerlist를 참고하여 level x+1의 answer를 작성
# level n이 될때까지
for x in range (0, n-1) : 
    for Qlist in answerlist[x] : 
        for Q in range(n) : 
            if Qlist_levelUP(Qlist, Q) != [0] :
                answerlist[x+1].append(Qlist_levelUP(Qlist, Q))

# level n의 해의 갯수 출력
print(len(answerlist[n-1]))