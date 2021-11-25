x, y = map(int, input().split())
daylist = [0,31,28,31,30,31,30,31,31,30,31,30,31]
sum = 0
for i in range(x) : 
    sum = sum + daylist[i]
sum = sum + y

if sum % 7 == 1 : 
    print('MON')
if sum % 7 == 2 : 
    print('TUE')
if sum % 7 == 3 : 
    print('WED')
if sum % 7 == 4 : 
    print('THU')
if sum % 7 == 5 : 
    print('FRI')
if sum % 7 == 6 : 
    print('SAT')
if sum % 7 == 0 : 
    print('SUN')