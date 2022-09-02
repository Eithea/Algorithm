before = list(input())
origin = ['((', '([', '[(', '[[', '))', ')]', '])', ']]', '()', '(]', '[)', '[]', ')(', ')[', '](', '][']
translation = [[2, 1], [2, 1], [3, 1], [3, 1], [2, -1], [3, -1], [2, -1], [3, -1], 2, 0, 0, 3, '+', '+', '+', '+']
trl = []
for i in range(len(before) - 1) : 
    for j in range(16) : 
        if before[i] + before[i+1] == origin[j] : 
            trl.append(translation[j])
# (()[[]])([]) -> 2*( 2 + 3*[ 3 ] ) + 2*( 3 )            
if len(trl) != len(before) - 1 : 
    trl = [0]

def calc(l) : 
    n = len(l)
    if 0 in l : 
        l = [0]
    else : 
        for i in range(n) : 
            if type(l[i]) is int and i > 0 and i < n - 1 : 
                if type(l[i-1]) is list and type(l[i+1]) is list :
                    if l[i-1][0] == l[i+1][0] and l[i-1][1] > l[i+1][1] : 
                        l[i] = l[i] * l[i-1][0]
                        l[i-1] = 'done'
                        l[i+1] = 'done'
            elif l[i] == '+' and i > 0 and i < n - 1 : 
                if type(l[i-1]) is int and type(l[i+1]) is int : 
                    l[i] = l[i-1] + l[i+1]
                    l[i-1] = 'done'
                    l[i+1] = 'done'
        while 'done' in l : 
            l.remove('done')

maxlen = 30
for i in range(maxlen//2) : 
    calc(trl)
if len(trl) == 1 and type(trl[0]) is int : 
    print(trl[0])
else : 
    print(0)