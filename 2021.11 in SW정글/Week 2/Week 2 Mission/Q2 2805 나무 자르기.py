n, m = map(int, input().split())
T = list(map(int, input().split()))
max = max(T)

def Bsearch(list, goal, lower, upper) : 
    if lower > upper : 
        return upper
    sum = 0
    center = (lower + upper) // 2
    for i in list : 
        if i > center : 
            sum = sum + i - center
    if sum == goal : 
        return center
    if sum > goal : 
        return Bsearch(list, goal, center + 1, upper)
    else : 
        return Bsearch(list, goal, lower, center -1)

print(Bsearch(T, m, 0, max))