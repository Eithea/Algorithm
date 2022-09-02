n = int(input())
square = []
for i in range(n) : 
    square.append(list(map(int, input().split())))

def detect(sq, size) : 
    for i in range(size) : 
        for j in range(size) : 
            if sq[i][j] != sq[0][0] : 
                return False
    return True

count = [0, 0]
def DAC(sq, size) : 
    if detect(sq, size) : 
        count[sq[0][0]] = count[sq[0][0]] + 1
    else : 
        DAC([sq[i][:size//2] for i in range(size//2)], size//2)
        DAC([sq[i][size//2:] for i in range(size//2)], size//2)
        DAC([sq[i][:size//2] for i in range(size//2, size)], size//2)
        DAC([sq[i][size//2:] for i in range(size//2, size)], size//2)

DAC(square, n)
print(count[0])
print(count[1])