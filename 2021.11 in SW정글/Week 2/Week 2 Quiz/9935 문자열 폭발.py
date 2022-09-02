word = input()
boom = list(input())

stack = []
count = 0
for i in range(len(word)) : 
    stack.append(word[i])
    if len(stack) >= len(boom) : 
        if stack[len(stack) - len(boom) :] == boom : 
            for i in range(len(boom)) : 
                del stack[-1]
if stack == [] : 
    print('FRULA')
else : 
    print("".join(stack))