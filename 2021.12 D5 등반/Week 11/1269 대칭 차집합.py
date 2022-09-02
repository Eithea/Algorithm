n1, n2 = map(int, input().split())
l1 = set(map(int, input().split()))
l2 = set(map(int, input().split()))

print(len(l1^l2))