def factorial(N):
    temp=1
    for i in range(1,N+1):
        temp*=i
    return temp

n,k=map(int,input().split())

if k==0:
    print(1)
else:
    print(int(factorial(n)/factorial(n-k)/factorial(k)))
