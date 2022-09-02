import sys
input = sys.stdin.readline

n = int(input())
l = [0]
for i in range(n) : 
    l.append(int(input()))

DP = [[0 for i in range(3)] for i in range(n + 1)]
# DP[i][x]는 거리 x(1 or 2)의 점프로 i번째에 들어온 경우의 최댓값
# [0] 안씀

DP[1][1] = l[1]
DP[1][2] = l[1]
if n > 1 : 
    DP[2][1] = l[1] + l[2]
    DP[2][2] = l[2]
# 자명해 입력

for i in range(3, n + 1) : 
    DP[i][1] = DP[i-1][2] + l[i]
    # i에 1의 점프로 들어왔다면 i-1에 들어온 이전 점프는 무조건 2
    DP[i][2] = max(DP[i-2][1], DP[i-2][2]) + l[i]
    # i에 2의 점프로 들어왔다면 i-2에 들어온 이전 점프는 1 or 2
print(max(DP[n]))