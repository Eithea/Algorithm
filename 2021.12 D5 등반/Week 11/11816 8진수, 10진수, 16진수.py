l = input()

card = 10
if len(l) > 2 and l[0:2] == '0x' : 
    l = l[2:]
    card = 16
elif len(l) > 1 and l[0] == '0' : 
    l = l[1:]
    card = 8

dic = {}
for i in range(10) : 
    dic[str(i)] = i
dic['a'] = 10
dic['b'] = 11
dic['c'] = 12
dic['d'] = 13
dic['e'] = 14
dic['f'] = 15

summ = 0
lenl = len(l)
for i in range(lenl) : 
    summ += dic[l[lenl-1-i]] * card **i
print(summ)