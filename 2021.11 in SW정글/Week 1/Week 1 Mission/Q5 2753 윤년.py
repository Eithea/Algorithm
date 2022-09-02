a = int(input())

if a%4 != 0 : 
    print(0)
elif a%100 == 0 and a%400 != 0 : 
    print(0)
else : 
    print(1)