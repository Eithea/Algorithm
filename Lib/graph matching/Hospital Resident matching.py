# condition
nH, nR = 5, 24
capH = 5

# input
pref_forRofH = [[i for i in range(nR)] for j in range(nH)]
priority_forHofR = [[i for i in range(nH)] for j in range(nR)]

class HOS() :
    def __init__(self, index, pref) : 
        self.index = index
        self.next = None
        self.cap = capH
        self.pref = pref
        self.stage = 0
        self.recruit = []

class RES() :
    def __init__(self, index, pr) : 
        self.index = index
        self.pr = pr
        self.match = -1

H = [None for i in range(nH)]
for i in range(nH) : 
    H[i] = HOS(i, pref_forRofH[i])
for i in range(nH-1) : 
    H[i].next = H[i+1]
H[nH-1].next = H[0]

R = [None for i in range(nR)]
for i in range(nR) : 
    R[i] = RES(i, priority_forHofR[i])


h = H[-1]
left = 74

i = 0
while left : 
    print(left, end = ' ')
    for hh in H : 
        print(hh.recruit, end = ' ')
    print()
    h = h.next
    if h.stage == len(h.pref) or len(h.recruit) == capH : 
        continue
    r = R[h.pref[h.stage]]
    while r.match >= 0 and r.pr[h.index] > r.pr[r.match] : 
        h.stage += 1
        r = R[h.pref[h.stage]]
        left -= 1
    if r.match >= 0 : 
        H[r.match].recruit.remove(r.index)
    r.match = h.index
    h.recruit.append(r.index)
    h.stage += 1
    left -= 1
        


# recruiting(H[-1], 23)
for h in H : 
    print(h.recruit)
for r in R : 
    print(r.match, end = ' ')
