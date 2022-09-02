n = int(input())
l = input()

def is_digit(x) : 
    if ord(x) < 48 or ord(x) > 57 : 
        return False
    return True

summ = 0
i = 0
connected = False
hdnum = ''
while i < n : 
    if is_digit(l[i]) : 
        hdnum += l[i]
        connected = True
    elif connected and not is_digit(l[i]) : 
        summ += int(hdnum)
        hdnum = ''
        connected = False
    i += 1
if connected : 
    summ += int(hdnum)

print(summ)
