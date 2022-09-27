import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())
for i in range(tc) : 
    n, target = map(int, input().split())
    l = list(map(int, input().split()))

    que = deque(l)
    l.sort(reverse=True)
    leng = len(l)
    prio = 0

    while True : 
        x = que.popleft()
        if x == l[prio] : 
            leng -= 1
            prio += 1
            if target : 
                target -= 1
            else : 
                print(prio)
                break
        else : 
            if not target :
                target += leng
            target -= 1
            que.append(x)