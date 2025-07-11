def factorial(N):
    if N==0:
        return 1

    temp=1
    for i in range(1,N+1):
        temp*=i
    return temp


N=int(input())
result=str(factorial(N))

index=-1
count=0
while True:
    if result[index]!='0':
        break
    else:
        count+=1
        index-=1

print(count)
