def Bsearch(list, target, start, end) : 
    if start > end : 
        return 0
    center = (start + end) // 2
    if target == list[center] : 
        return 1
    if target < list[center] : 
        return Bsearch(list, target, start, center - 1)
    if target > list[center] : 
        return Bsearch(list, target, center + 1, end)

n = int(input())
unsortedA = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))
A = sorted(unsortedA)
n = len(A) - 1
for i in mlist : 
    print(Bsearch(A, i, 0, n))