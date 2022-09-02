n = int(input())

apple = []
k = int(input())
for i in range(k) : 
    y, x = map(int, input().split())
    apple.append([y, x])

order = []
l = int(input())
for i in range(l) : 
    X, C = input().split()
    order.append([int(X), C])

right = [0, 1]
# down = [1, 0]
# left = [0, -1]
# up = [-1, 0]
def drift(d, lr) : 
    if lr == 'D' : 
        return [d[1], -d[0]]
    if lr == 'L' : 
        return [-d[1], d[0]]

snake = [[1,1]]
direction = right
t = 0
while True : 
    t = t + 1
    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    if head[0] == 0 or head[0] == n+1 or head[1] == 0 or head[1] == n+1 or head in snake : 
        print(t)
        break
    snake.insert(0, head)
    if head in apple : 
        apple.remove(head)
    else : 
        del snake[-1]
    if [t, 'L'] in order : 
        direction = drift(direction, 'L')
    if [t, 'D'] in order : 
        direction = drift(direction, 'D')