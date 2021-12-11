def DAC(start, end) :
    if start == end :
        return A[start] ** 2
        
    center = (start + end) // 2
    maxscore = max(DAC(start, center), DAC(center+1, end))

    left = center
    right = center + 1
    w = A[left] + A[right]
    h = min(A[left], A[right])
    maxscore = max(maxscore, h * w)
    while start < left or right < end:
        if right < end and (left == start or A[left-1] < A[right + 1]) :
            right += 1
            w += A[right]
            h = min(h, A[right])
        else :
            left -= 1
            w += A[left]
            h = min(h, A[left])
        maxscore = max(maxscore, h * w)
    return maxscore

n = int(input())
A = list(map(int, input().split()))
print(DAC(0, n-1))