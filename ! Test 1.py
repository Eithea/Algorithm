n = 5
I = [[0 for i in range(n)] for j in range(n)]
A = [I[i][:] for i in range(n)]
print(*A)