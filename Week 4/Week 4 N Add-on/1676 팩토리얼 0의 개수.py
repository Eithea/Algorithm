n = int(input())
count2 = 0
pow2 = 2
while pow2 <= n : 
    count2 = count2 + n // pow2
    pow2 = pow2 * 2
count5 = 0
pow5 = 5
while pow5 <= n : 
    count5 = count5 + n // pow5
    pow5 = pow5 * 5
print(min(count2, count5))