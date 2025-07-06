N=int(input())

n=m=count=1

while(n<= 1000000000):
    if n<=N and N<=m:
        print(count)
        break
    else:
        n=m+1
        m=m+6*(count)
        count+=1

