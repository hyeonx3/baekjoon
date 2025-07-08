A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    day = A - B
    temp = (V - A + day - 1) // day 
    print(temp + 1)
