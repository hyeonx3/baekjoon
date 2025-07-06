import math

def is_prime(N):
    if N==1:
        return 0
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0:
            return 0
        
    return 1

N=int(input())
num=list(map(int,input().split()))

count=0
for n in num:
    if is_prime(n)==1:
        count+=1

print(count)

