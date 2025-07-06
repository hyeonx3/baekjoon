import math

N=int(input())
size=list(map(int, input().split()))
t,p=map(int, input().split())


shirt=sum(math.ceil(i/t) for i in size)
pen1=N//p
pen2=N%p

print(shirt)
print(pen1, pen2)