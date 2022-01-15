D=[1,0,3]+[0]*28
for i in range(4,31):D[i]=4*D[i-2]-D[i-4]
print(D[int(input())])