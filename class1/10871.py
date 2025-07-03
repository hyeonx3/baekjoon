N, X = map(int, input().split())
lst = list(map(int, input().split()))
print(' '.join(str(i) for i in lst if i < X))
