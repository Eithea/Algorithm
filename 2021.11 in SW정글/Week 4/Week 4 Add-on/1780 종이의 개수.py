n = int(input())
square = []
for i in range(n) : 
    square.append(list(map(int, input().split())))

def detect(sq, size, x, y) : 
    for i in range(size) : 
        for j in range(size) : 
            if sq[x+i][y+j] != sq[x][y] : 
                return False
    return True

count = [0, 0, 0]
def DAC(sq, size, x, y) : 
    if detect(sq, size, x, y) : 
        count[sq[x][y]] = count[sq[x][y]] + 1
    else : 
        DAC(sq, size//3, x, y)
        DAC(sq, size//3, x+size//3, y)
        DAC(sq, size//3, x+2*size//3, y)
        DAC(sq, size//3, x, y+size//3)
        DAC(sq, size//3, x+size//3, y+size//3)
        DAC(sq, size//3, x+2*size//3, y+size//3)
        DAC(sq, size//3, x, y+2*size//3)
        DAC(sq, size//3, x+size//3, y+2*size//3)
        DAC(sq, size//3, x+2*size//3, y+2*size//3)
        
DAC(square, n, 0, 0)
print(count[-1])
print(count[0])
print(count[1])