import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n, k = map(int, input().split())

N = []
for i in range(n) : 
    N.append(list(map(int, input().split())))
N.sort()

K = []
for i in range(k) : 
    K.append(int(input()))
K.sort()

sumv = 0
i = 0
heap = []
#무게 오름차순으로 정렬된 가방, 보석에서 for문 실행
for bag in K : 
    while i < n and N[i][0] <= bag : 
        heappush(heap, -N[i][1])
        i = i + 1
    # 가방에 담을 수 있는 모든 보석을 heap에 넣는다
    if heap != [] : 
        sumv = sumv - heappop(heap)
    # 가장 비싼 보석은 pop해서 sum에 더한다
    # 나머지 보석은 다음 가방(무게가 더 큰 가방)에도 담기므로 for문의 다음 bag에 그대로 들고간다
print(sumv)