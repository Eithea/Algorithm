testcase = int(input())
l = []
for i in range(testcase) : 
    word = input()
    if word not in l : 
        l.append(word)

l.sort()
l.sort(key = len)

for i in l:
    print(i)