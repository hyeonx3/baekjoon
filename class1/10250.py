import math

n=int(input())
lst=[]

for i in range(n):
    H,W,N=map(int,input().split())
    room=str(math.ceil(N/H)).zfill(2)
    floor=str(H if N%H==0 else N%H)

    lst.append(floor+room)

print(*lst, sep='\n')


