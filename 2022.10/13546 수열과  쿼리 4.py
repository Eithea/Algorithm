import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
A = list(map(int, input().split()))
m = int(input())

Q = []
for i in range(m) : 
    l, r = map(int, input().split())
    Q.append([l-1, r-1, i])

sqn = int(n**0.5) +1
Q.sort(key = lambda x : x[0])
Q.sort(key = lambda x : x[1] //sqn)

distribution = [0 for i in range(n+1)]
bucket = [0 for i in range(n//sqn +1)]

deques = [deque() for i in range(k+1)]


def distribution_push(x) : 
    distribution[x] += 1
    bucket[x//sqn] += 1

def distribution_pop(x) : 
    distribution[x] -= 1
    bucket[x//sqn] -= 1

def deque_push_left(x) : 
    que = deques[A[x]]
    if que : 
        distribution_pop(que[-1] - que[0])
    que.appendleft(x)
    distribution_push(que[-1] - que[0])

def deque_push_right(x) : 
    que = deques[A[x]]
    if que : 
        distribution_pop(que[-1] - que[0])
    que.append(x)
    distribution_push(que[-1] - que[0])

def deque_pop_left(x) : 
    que = deques[A[x]]
    distribution_pop(que[-1] - que[0])
    que.popleft()
    if que : 
        distribution_push(que[-1] - que[0])

def deque_pop_right(x) : 
    que = deques[A[x]]
    distribution_pop(que[-1] - que[0])
    que.pop()
    if que : 
        distribution_push(que[-1] - que[0])


def find() : 
    for i in reversed(range(len(bucket))) : 
        if not bucket[i] : 
            continue
        for j in reversed(range(sqn)) : 
            idx = i*sqn +j
            if idx > n : 
                continue
            if distribution[idx] : 
                return idx
    return 0

ans = [None for i in range(m)]

pl, pr = Q[0][0], Q[0][0] -1
for l, r, i in Q : 
    while l < pl : 
        pl -= 1
        deque_push_left(pl)
    while r > pr : 
        pr += 1
        deque_push_right(pr)
    while l > pl : 
        deque_pop_left(pl)
        pl += 1
    while r < pr : 
        deque_pop_right(pr)
        pr -= 1
    ans[i] = find()

print(*ans, sep = '\n')